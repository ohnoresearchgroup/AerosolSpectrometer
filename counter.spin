''Using the Propeller to count pulses
CON 
        'Run at 80_000_000 MHz
        _clkmode = xtal1 + pll16x
        _XinFREQ = 5_000_000
        
CON
        rx_pin  = 31        ' Propeller RX pin
        tx_pin  = 30        ' Propeller TX pin
        baud = 115200       ' Optimum Baud Rate for PC application
        mode    = %0000     ' Serial Port mode (See FullDuplexSerial.spin) 

OBJ
        'Import serial module for communications with host
        serial :   "FullDuplexSerial"
        
VAR
        byte cmd 'byte to store serial command

'main method to execute
PUB main | data
        
        'initialize serial comms
        serial.start(rx_pin, tx_pin, mode, baud) 
        
        'enter loop to check if it has received any commands
        repeat
            serial.rxflush              'flush buffer
            cmd := serial.rxtime (100)  'wait for byte
        
            if cmd == "C"                   'command to check status
                serial.Tx ("G")             'send command that it is good
            
            elseif cmd == "D"               'command to get data           
                cognew(@entry, @data)       'start cog to count for 1 s
                waitcnt(cnt + clkfreq + 32) 'wait 1 s + 32 extra cycles   
                serial.dec(data)            'send data
                                  
'assembly code for running counter
DAT
        org     

entry   mov     ctra, ctra_             'establish mode and start counter
        mov     frqa, #1                'increment by 1 for each edge seen
        mov     cnt_, cnt               'record time to measure from
        add     cnt_, cntadd            'sum cnt and cntadd so know what clock cycle to wait for
        waitcnt cnt_, cntadd            'wait for next sample (delta doesn't matter here)
        mov     new, phsa               'record new count
        wrlong  new, par                'write new count to address given when called          
        cogid   myid                    'get the ID of the cog I'm running in	
        cogstop myid                    'use the ID to terminate myself
        
ctra_   long    %01010 << 26 + 7        'posedge mode + APIN (PIN is 7)
cntadd  long    80_000_000              'count for 1 second 

cnt_    res     1
new     res     1
myid    res     1