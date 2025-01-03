#  Data Structures and Algorithm

always remember data structure and algorithm are both connected

**Q1- what is Data Structure ?** <br />
**A1-** Structure of the Data, can be anything, most commonly use are:
- **string** ( any character )
- **number/integer** ( any number )
- **boolean** ( true and false )
- **null** ( kinda hard to explain - let's say value is nothing - type is specified - not true in some cases )
- **undefined** ( same as null but value is not been removed or never specified )
- **object** ( combination of other data types )
- **array** ( list of other data types )

**Q2- what is algorithm ?** <br />
**A2-** Algorithm is in simple a step to do anything, like a recipe to cake, but what it do with data so in this situation we can say algorithm is the way to step of code you write to achieve the business logic.

**Q3- what is time complexity ?** <br />
**A3-** The amount of time an algorithm wll take to complete - it will measure with Big O.

**Q4- what is n ?** <br />
**A4-** n is usually use for length of the data.

**Q5- what is big O ?** <br />
**A5-** Big O describe as performance of an algorithm. it usually describe worst-case scenario of the algorithm

**Q6- what is big O(n) - {o of n} ?** <br />
**A6-** O(n) or {o of n} is when algorithm run the length of the array
- **note:** both example are using liner search
- **eg-1:** find the number 3
    - **equation-1:** list = 9, 2, 3, 5, 2, 1
        - **why it's O(n)-1:** in this scenario list will run and check every number until it will find 3 and the worst case it will be the end and best it will be the first but we have to follow worst so it will be O(n)
        -  **solution-1:** we will go through every number and check if this number is 3 and if yes then we will return it otherwise move to next number
- **eg-2:** find smallest number of the array of number
    - **equation-1:** list = 9, 2, 3, 5, 2, 1
        - **why it's O(n)-1:** in this scenario list will run maximum the number of the array and check every number one by one to find minimum number and this is O(n)
        -  **solution-1:** well solution will go something like this you save the first value in a variable then compare it wil second value and if the value is less then second value then update the variable value and in both cases move to next until list end and in the end return the value of the variable

**Q7- what is O(1) - {O of 1} ?** <br />
**A7-** O(1) of {O of 1} - is when you have to run only one cycle to get the result also know as **constant time**. like in O(n) - n is the length which will define how many time the process will run same here O(1) - 1 is telling that the process will only run 1 time. it will work only with few situation, let's say you have an object or an array
- **eg-1:** O(1) with an hashmap(object)
    - **equation-1:** hashmap = { name: "Mohammad Moiz Ali", age: 23 }
        - **why it's O(1)-1:** in this kind of hashmap you can just use hashmap name with the name of the kay - (hashmap.name || hashmap['name']) and you will get your result, so as you can we we don't have to go through the complete object and look for every key like in O(n) and it's only possible because we are using an hashmap (which is an object in most of the cases) - and you will only use one cycle and get the response so it's O(1)
- **eg-1:** O(1) with an array
    - **equation-1:** list = 9, 2, 3, 5, 2, 1
        - **why it's O(1)-1:** you can only apply O(1) in an array when you want on which index you want to go like if you want second index you can say something like this list[1] = (array usually start with 0 so first index is 0 and second is 1) and here you can also look it's again just one cycle so that's why it's O(1)
- **note:** O(1) will only work in this 2 situation with specific needs and specific data types (and that's why we say in the start that data structure and algorithm are connected because if data will in different form then you can't use O(1))

**Q8- what is O(log n) ?** <br />
**A8-** O(log n) is when you will eliminate half of the length in every cycle - a common example is binary search - I know answer is not self explanatory but if you understand binary search we can understand O(log n) easily
- their are tow requirement to implement O(log n)
    - list should be sorted
    - your requirement is to find something
- if we the root of the length of the list we know how much a O(log n) will run like if list length is 16 then O(log n) will run only 4 time in worst scenario
- in mathematical terms we can say: `log2(16) = 4` or `2x = 16` where `x is 4`

**Q9- what is Binary Search ?** <br />
**A9-** Binary Search in simple term is divide by 2 and check until you find your value (only work with sorted array) - you take a sorted value and your goal is to find the number (let's say it's 100) so you start with the middle value (length of the list divide by 2) and check if the value you are looking is same of not and if it then stop, you got the solution otherwise check if the value (that you are looking)  is smaller or larger then the middle value if it's smaller then move to right side otherwise move to left and repeat the process until you find the value
- **equation-1** list = 1, 2, 4, 5, 9, 10, 23, 35, 60, 100, find=100
    - **requirements:** first the list should be sorted, second you need to find some value not do sorting or other kind of stuff
    - **why it's a binary search:**  you check the requirement does you want to find a value or not and if yes you check if array is sorted and if both things match you can apply binary search
    - **solution-1** first we count list length which is 10 so we get the value of 5th value which is 9 and check if it's 100 then we know it's not then we will move our focus on the right side **(10, 23, 35, 60, 100)** and count the length which is 5 now so we go check the 3 member value of the list which is 35 again it's less then 100 so we again focus on the right side **(60, 100)** and now we only have two value left and repeat the process and check 60 and again 60 is less then 100 so we check the last value **(100)** and if it's match then we will return the last value

**Q10- what is O(n^2) - { O n square } ?** <br />
**A10-** O(n^2) - { O n square } - in simple words for every element check each element - and a nested loop is also a O(n^2) time complexity.
- the maximum number of cycle it will run will be the square of n - so if n is 10 worst it will go for 100
- **example-1:** you have to sort an array without creating a new array so what you will do, let's say your list is **(9, 7, 5, 3, 1, 8, 4, 2, 6, 0)**. so you check the first value and keep if to it's place and you move to second and compare if first value if less then second then you switch second value to first place and if not keep it in the second place **(7, 9, 5, 3, 1, 8, 4, 2, 6, 0)**, next you match the third value with second and if its less then second you compare if with first, if it's greater then second you will keep it in third place if its bigger then first and less then second you add it in second and current second will be become first and if value is less then first then it will become first and current first and second will become second and third **(5, 7, 9, 3, 1, 8, 4, 2, 6, 0)** and you will repeat this process until the end
- **example-2:** you get two list, list1 is **(1, 2, 3, 4, 5, 6, 7, 8, 9)** and list2 is **(9, 7, 5, 3, 1)** and now your task is to return same value in both array - what you can do is take first value from list1 and compare it will every value present in list2
- in mathematical term we can say n2 = (10)2 = 10 X 10 = 100

**Q11- what is insertion sort ?** <br />
**A11-** insertion sort - imagine you have a list as 6, 5, 3, 1, 8, 7, 2, 4. so in insertion sorting you will take first value and check before it nothing so you put it there, now move to second number and you see, 5 is less then 6 so you move 5 before 6, next move to third number and see 3 is less then 6 and again less then 5 as well, so you move 3 in the top and repeat the process for each number.
- time complexity: **O(n^2)**
