
In [1]: type(99.9)                                                                                   
Out[1]: float

In [2]: type("False")                                                                                
Out[2]: str

In [3]: type(False)                                                                                  
Out[3]: bool

In [4]: type('0')                                                                                    
Out[4]: str

In [5]: type(0)                                                                                      
Out[5]: int

In [6]: type(True)                                                                                   
Out[6]: bool

In [7]: type('True')                                                                                 
Out[7]: str

In [8]: type([{}])                                                                                   
Out[8]: list

In [9]: type({'a': []})                                                                              
Out[9]: dict

In [16]: str                                                                                         
Out[16]: str

In [17]: bool                                                                                        
Out[17]: bool

In [18]: float                                                                                       
Out[18]: float

In [19]: bool                                                                                        
Out[19]: bool

In [20]: str                                                                                         
Out[20]: str

In [21]: float                                                                                       
Out[21]: float

In [22]: list                                                                                        
Out[22]: list

In [23]: str                                                                                         
Out[23]: str

In [24]: str                                                                                         
Out[24]: str

In [25]: '1' + 2                                                                                     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-25-20b2518fe802> in <module>
----> 1 '1' + 2

TypeError: can only concatenate str (not "int") to str

In [26]: 6 % 4                                                                                       
Out[26]: 2

In [27]: type(6 % 4)                                                                                 
Out[27]: int

In [28]: type(type(6 % 4))                                                                           
Out[28]: type

In [29]: '3 + 4 is ' + 3 + 4                                                                         
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-d779031f2239> in <module>
----> 1 '3 + 4 is ' + 3 + 4

TypeError: can only concatenate str (not "int") to str

In [30]: 0 < 0                                                                                       
Out[30]: False

In [31]: 'False' == False                                                                            
Out[31]: False

In [32]: True == 'True'                                                                              
Out[32]: False

In [33]: 5 >= -5                                                                                     
Out[33]: True

In [34]: !False or False                                                                             

In [35]: True or "42"                                                                                
Out[35]: True

In [36]: !True && !False                                                                             
zsh:1: command not found: !False

In [37]: !True && !False                                                                             
zsh:1: command not found: !False

In [38]: 6 % 5                                                                                       
Out[38]: 1

In [39]: 5 < 4 and 1 == 1                                                                            
Out[39]: False

In [40]: 'codeup' == 'codeup' and 'codeup' == 'Codeup'                                               
Out[40]: False

In [41]: 4 >= 0 and 1 !== '1'                                                                        
  File "<ipython-input-41-28fe0c9082c3>", line 1
    4 >= 0 and 1 !== '1'
                   ^
SyntaxError: invalid syntax


In [42]: 6 % 3 == 0                                                                                  
Out[42]: True

In [43]: 6 % 3                                                                                       
Out[43]: 0

In [44]: 5 % 2 != 0                                                                                  
Out[44]: True

In [45]: [1] +2                                                                                      
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-45-e6465c012b73> in <module>
----> 1 [1] +2

TypeError: can only concatenate list (not "int") to list

In [46]: [1] + 2                                                                                     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-46-54324b7054ad> in <module>
----> 1 [1] + 2

TypeError: can only concatenate list (not "int") to list

In [47]: [1] + [2]                                                                                   
Out[47]: [1, 2]

In [48]: [1] * 2                                                                                     
Out[48]: [1, 1]

In [49]: [1] * [2]                                                                                   
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-49-887f6473eaff> in <module>
----> 1 [1] * [2]

TypeError: can't multiply sequence by non-int of type 'list'

In [50]: [] + [] == []                                                                               
Out[50]: True

In [51]: {} + {}                                                                                     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-51-03eea6c7a00d> in <module>
----> 1 {} + {}

TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

In [54]: little_mermaid = 3                                                                          

In [55]: brother_bear = 5                                                                            

In [56]: hercules = 1                                                                                

In [57]: (little_mermaid + brother_bear + hercules) * 3                                              
Out[57]: 27

In [58]: google = 400                                                                                

In [59]: amazon = 380                                                                                

In [60]: facebook = 350                                                                              

In [61]: (facebook * 10) + (google * 6) + (amazon * 4)                                               
Out[61]: 7420

In [65]: class_full = False                                                                          

In [66]: class_schedule_conflict = False                                                             

In [67]: student_enrolled = class_full AND class_schedule_conflict                                   
  File "<ipython-input-67-db42cff7af86>", line 1
    student_enrolled = class_full AND class_schedule_conflict
                                    ^
SyntaxError: invalid syntax


In [68]: student_enrolled = class_full + class_schedule_conflict                                     

In [69]: student_enrolled == class_full + class_schedule_conflict                                    
Out[69]: True