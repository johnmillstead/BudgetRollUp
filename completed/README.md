# BudgetRollUp
This script is used to roll-up individual departmental budgets into a single, master budget.

Files are initially emailed in to the Operations Manager.

The Operations Manager will pre-process the files by saving as xlsx instead of xlsm and will split out the appropriate 'budget' sheet.  All links to dependant files are also broken.

Files are then saved into the *Completed* directory and renamed to departmentname.xlsx

