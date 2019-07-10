''Using the Propeller to count pulses
CON 
        'Run at 80_000_000 MHz
        _clkmode = xtal1 + pll16x
        _XinFREQ = 5_000_000
OBJ
        'Import serial module for communications with host
        pst :   "FullDuplexSerial"

'main method to execute
PUB main | data, cmd
        'Initialize serial communications at baudrate of 115200
        pst.start (31, 30, 0, 115200)
        
        'enter loop to check if its received command
        repeat
            pst.RxFlush
            cmd := pst.RxTime (100) 'check if its received serial command to get data
        
            if cmd == %00110000  'if it has
                'start a cog to count
                cognew(@entry, @data)
                waitcnt(cnt + clkfreq + 32)        
                pst.dec(data)
                                  
'assembly code for running counter
DAT
        org     

entry   mov     ctra, ctra_             'establish mode and start counter
        mov     frqa, #1                'increment by 1 for each edge seen
        mov     cnt_, cnt               'setup time delay to measure from
        add     cnt_, cntadd            '??
        waitcnt cnt_, cntadd            'wait for next sample (delta doesn't matter here)
        mov     new, phsa               'record new count
        wrlong  new, par                             
        cogid   myid                    'get the ID of the cog I'm running in	
        cogstop myid                    'use the ID to terminate myself
        
ctra_   long    %01010 << 26 + 7        'posedge mode + APIN (PIN is 7)
cntadd  long    80_000_000              'count for 1 second 

cnt_    res     1
new     res     1
myid    res     1