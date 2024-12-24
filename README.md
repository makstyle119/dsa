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
- **eg-1:** find the number 3
    - **equation-1:** list = 9, 2, 3, 5, 2, 1
        - **why it's O(n)-1:** in this scenario list will run and check every number until it will find 3 and the worst case it will be the end and best it will be the first but we have to follow worst so it will be O(n)
        -  **solution-1:** we will go through every number and check if this number is 3 and if yes then we will return it otherwise move to next number
- **eg-2:** find smallest number of the array of number
    - **equation-1:** list = 9, 2, 3, 5, 2, 1
        - **why it's O(n)-1:** in this scenario list will run maximum the number of the array and check every number one by one to find minimum number and this is O(n)
        -  **solution-1:** well solution will go something like this you save the first value in a variable then compare it wil second value and if the value is less then second value then update the variable value and in both cases move to next until list end and in the end return the value of the variable

**Q7- what is O(1) - {O of 1} ?** <br />
**A5-** O(1) of {O of 1} - is when you have to run only one cycle to get the result also know as **constant time**. like in O(n) - n is the length which will define how many time the process will run same here O(1) - 1 is telling that the process will only run 1 time. it will work only with few situation, let's say you have an object or an array
- **eg-1:** O(1) with an hashmap(object)
    - **equation-1:** hashmap = { name: "Mohammad Moiz Ali", age: 23 }
        - **why it's O(1)-1:** in this kind of hashmap you can just use hashmap name with the name of the kay - (hashmap.name || hashmap['name']) and you will get your result, so as you can we we don't have to go through the complete object and look for every key like in O(n) and it's only possible because we are using an hashmap (which is an object in most of the cases) - and you will only use one cycle and get the response so it's O(1)
- **eg-1:** O(1) with an array
    - **equation-1:** list = 9, 2, 3, 5, 2, 1
        - **why it's O(1)-1:** you can only apply O(1) in an array when you want on which index you want to go like if you want second index you can say something like this list[1] = (array usually start with 0 so first index is 0 and second is 1) and here you can also look it's again just one cycle so that's why it's O(1)
- **note:** O(1) will only work in this 2 situation with specific needs and specific data types (and that's why we say in the start that data structure and algorithm are connected because if data will in different form then you can't use O(1))


