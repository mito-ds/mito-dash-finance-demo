# Demo Overview

This is a simple demo that shows how to use Mito to automate standard financial reporting. In the demo, we use a combination of spreadsheet formulas (VLOOKUP) and pivot tables to calculate the average MoM returns for a set of Vanguard mutual funds. 

# Demo Instructions

1. Launch the Dash app
2. In the second dataframe in Mito, 
    * Add a new column
    * Name it "Managers"
    * Use the VLOOKUP formula to pull the manager name from the first dataframe: `=VLOOKUP(Fund0,df1!Fund Name:Portfolio Manager, 2)`
3. Show the generated code that Mito created and mention: "Mito generates the equivalent Python code for every edit you make in the spreadsheet."
4. Create a pivot table with the following configuration:
    * Dataframe: df2
    * Rows: "Fund" and "Manager"
    * Columns: "Date" (Grouped by Year)
    * Values: "MoM Return" with an aggregation of mean
5. Show the generated code and mention: Now that you've created the report in Mito, the generated Python code can be used to rebuild this report over and over again with just the click of a button. As the analyst, you can use Mito to automate your reporting without needing to learn Python. As the app developer you can:
    * Give your users full Excel-like ability to customize/edit their data without leaving your Dash app.
    * Save the Mito generated code and use it to automate the report creation
    * Use the generated code to repopulate the app the next time the user opens it, 
    * Use Mito as a way to convert the business logic only known by the analyst into python code that is useful to a data science team.
    * etc.

# Questions?

If you have questions about this app, just [reach out to the Mito team](mailto:founders@sagacollab.com).