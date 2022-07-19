## Connecting to MySQL from Unix/Linux :

If we are going to  connect to MySQL from  Unix  , after successful login to MySQL, one can connect to the server from any directory.

Use the below command to connect to the MySQL server :

                       mysql -u username  -p 

For example, if user name is “user1” , then the command to be provided is :

                       mysql -u user1 -p

Once we provide this command the shell prompts to enter the password. provide the password and you should see the **(>mysql)** prompt if the connection is successful.
 

Once you are connected to the server, you need to create a new database or select an existing one to proceed.

Suppose you already have a database with the name "test" created, then you can connect to your database as,

                           mysql>use test;

## Connecting to MySQL from Windows :     

In windows, you can connect/use MySQL using any one of the following utilities :

- a. MySQL Command Line Client

- b. MySQL Workbench

a. If you use, the command line client , you will be prompted to provide your username and password. Once the correct details are provided, you will be able to use the server after selecting/creating a database as mentioned in the above section.

b. If you use the MySQL Workbench, you need to click on MySQL connections and then follow the below mentioned steps. Please refer to the below screen shot for the steps.

![MySQL Workbench steps](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/3527/image_4162_original.png "MySQL Workbench steps")

C:\Users\hp\VScodium Programs\VSCodium\Conecting to Database.md