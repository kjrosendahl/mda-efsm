# MDA-EFSM
## CS 586: Project 2, Part 2 
### Kaylee Rosendahl 

Project source code and executable for the MDA-EFSM for two implementations of Vending Machines, VM1 and VM2.

The driver executable can be found in the *dist* folder.

Source code, surprisingly, can be found in the *source-code* folder. 

#### File Breakdown: 
- **driver.py**: Program which runs the different implementation of vending machines. Upon running, will allow the user to create one of two available machines, then display a menu of operations from which the user many interact with. 
- **vm.py**: IP for VM1 and VM2. 
- **data.py**: Data stores D1, D2 for VM1, VM2, respectively. 
- **mda.py**: MDA-EFSM and MDA-EFSM states. Falls under the **state** pattern. 
- **absfact.py**: Abstract Factory, concrete factories CF1, CF2 for VM1, VM2, respectively. Falls under the **abstract factory** pattern. 
- **op.py**: OP which carries out meta-actions. Falls under the **abstract factory** and **strategy** patterns. 
- **actions.py**: Actions triggered by OP. Each abstract class has two stategies, one for each of the VMs. Falls under the **strategy** pattern.
