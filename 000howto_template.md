# how-to :: Use margins and padding in CSS
---
## Overview
Margins and padding allow us to format elements on websites, specifically to put space between different elements and blocks of text.

### Estimated Time Cost: x.x hrs

### Prerequisites:

- Basic knowledge of html and CSS.
    - Knowledge of settign up external CSS.
- Nothing.

1. Set up a basic html file and a basic CSS file, and link them together using this syntax:
```
    <head>
        <link
        rel = "stylesheet"
        type = "text/css"
        href = "filename"  
        >
    </head>
```
NOTE: If your html and CSS files are stored in different directories, "filename" must include the path to the CSS file from the directory where your html file is being stored.

2. Tag your elements under classes, depending on how your want your webpage grouped.

3. Open your html file in your browser.

4. Margins add space between different elements. Margins for each side can be changed individually. By default, all elements have some margin spacing between them, but this can be changed by following any of these steps:
    a. Use
        ```
        class{
            margin: 25px;
        }
        ```
        To set the width of margins on all four sides of the element to 25 pixels.

    b. Use
        ```
        class{
            margin: 25px 50px;
        }
        ```
        To set the top and bottom margins to 25px, and the right and left margins to 50 pixels wide.

    c. Use
        ```
        class{
            margin: 25px 50px 75px;
        }
        ```
        To set the top margin to 25 pixels, right and left to 50 pixels, and the bottom margin to 75 pixels wide.

    d. Use
        ```
        class{
            margin: 25px 50px 75px 100px;
        }
        ```
        To set the top margin to 25 pixels, the right to 50 pixels, the bottom to 75 pixels, and the left to 100 pixels wide.

    e. Use
        ```
        margin-top: 25px
        margin-right: 25px
        margin-bottom: 25px
        margin-left: 25px
        ```
        To set the width of each margin individually.

    NOTE: Percentages (ie: margin: 25%) can be used instead of the number of pixels to make it such that the margins will scale with the window size. The percentages used will be in reference to element containing the class being modified.

5. Padding adds space between the edges of an element and the text it contains. Padding for each side can be changed individually. By default all elements have no padding, but that can be changed by following any of these steps:

1. Step, with
    ```
    generic code block or terminal command
    ```
   and/or...
    ```javascript
    var foo = "this that JS tho";
    ```
   and/or...
    ```python
    print("this that Python tho")
    ```
   and/or...
1. Step, with [hyperlink](https://xkcd.com)s...


### Resources
* thing1
* thing2

---

Accurate as of (last update): 2022-mm-dd

#### Contributors:  
Clyde "Thluffy" Sinclair  
Thundercleese, pd2  
Buttercup, pd7  
Blossom, pd7  
Bubbles, pd7  
Fake Grimlock, pd8  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
