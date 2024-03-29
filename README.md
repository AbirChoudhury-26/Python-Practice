# This Series includes Python Concepts.
**General Topics:** 
 - Arrays
 - Tuples 
 - List
 - Dictionary
 - String Manipulation
 - Sets , Matrix Logics etc.

**Searching & Sorting:**
 - Linear
 - Buuble 
 - Selection
 - Insertion

 **Pattern Printing Types:**
 - Diamond & Half-Diamond
 - Double Sided Star
 - Inverted Star

 **OOPs Concept:**
 - Encapsulation
 - Inheritance
 - Polymorphism
 - Super Functions
 
### In this Series ,Selenium+Python is Practiced.

 | **WebDriver Functions**  | **Selenium Methods** | **Usage**
 |--------------|----------------|--------------|
 | find_element | Use of Link-Text,Id,Name,Clas,XPath | To find Elements from HTML DOM 
 | Exceptions   | ElementNotSelectableException       | Thrown when trying to select an unselectable element.
 |              | NoSuchElementException              | Thrown when element couldn't be found
 |              | ElementNotVisibleException          | Thrown when existing element in DOM has a feature set as hidden     
 |              | ElementNotInteractableException     | Thrown when element is presented in DOM impossible to interact it.
 |              | ElementClickInterceptedException    | Thrown when element cant be completed as the element receiving the events.
 |              | WebDriverException                  | Thrown when WebDriver is performing action right after browser is closed.
 |              | TimeoutException                    | Thrown when there is not enough time for a command to be completed.
 | sendKeys()   | This method enters a value in to an Edit Box or Text box. | **Syntax:** driver.findElement(By.elementLocator(“value”)).sendkeys(“value”); 
 | clear()      | It clears the Value from an Edit box or Text Box.         | **Syntax:** driverObject.findElement(By.locatorname(“value”)).clear();
 | click()      | It clicks an Element (Button, Link, Checkbox) etc.        | **Syntax:** driverObject.findElement(By.ElementLocator(“LocatorValue”)).click();
 | close()      | This command close the current browser window in focus.   | **Syntax:** driver.close();
 | quit()       | This method closes all browser windows which are opened.Terminates the WebDriver session. |   **Syntax:** driver.quit();
 | back()       | The back command instruct browser to redirect to previous webpage | **Syntax:** driver.navigate().back();
 | Implicit wait| WebDriver waits until condition occurs before throwing exception | **Syntax:** driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
 | Explicit wait| WebDriver waits until a condition occurs after executing further | **Syntax:** WebDriverWait wait = new WebDriverWait(driver,30);
 | getAttribute() | The command helps to view the value type in a search text box. | **Syntax:** findElement(By.xpath(“XPATHVALUE")).getAttribute(“Attributevalue");
 | isSelected() | The command helps to verify if they have been selected or not | **Sysntax:** element.isSelected();



 

