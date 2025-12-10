# binary-search-firas
---
title: Binary Search Firas
emoji: 🐨
colorFrom: pink
colorTo: pink
sdk: gradio
sdk_version: 6.1.0
app_file: app.py
pinned: false
---
## Binary Search Visualizer for CISC 121 Project


## Demo video/gif/screenshot of test
1. Case 1 where target in the middle
   - input list: 10 24 46 53 67 120 abd target is`67`
   - result showed 3 steps and reported 67 has been FOUND at index 4.  
  

![Screenshot 2025-12-09 at 9.48.47 PM](https://cdn-uploads.huggingface.co/production/uploads/6938eba830ae9cd28790f5b7/bChlnlw7j83SWHnMhJs2p.png)

2. Casw 2 where target not in the list
   - Input list 10 24 46 53 67 120 with a target value 99
   - result showed steps then final message  
     ERROR: Your entered target value of 99 does not exist in the given list.
     

![Screenshot 2025-12-09 at 9.49.19 PM](https://cdn-uploads.huggingface.co/production/uploads/6938eba830ae9cd28790f5b7/SfCSAkE8jRc7Sau4El33V.png)

3. Case 3 Unsorted list
   - input list that isnt sorted like 10 5 20 with target valye of 5
   - result immediately showed 
     ERROR: the list must be sorted in non-decreasing (ascending) order.

![Screenshot 2025-12-09 at 9.49.55 PM](https://cdn-uploads.huggingface.co/production/uploads/6938eba830ae9cd28790f5b7/O8j6LP_oHHtkUE38a4SSk.png)

4. Case 4 Invalid list input
   - input list of 10 a 20
   - Target:20
   - result gave me an error again 
     `ERROR: list should only have whole numbers separated by spaces and no commas.`

![Screenshot 2025-12-09 at 9.50.15 PM](https://cdn-uploads.huggingface.co/production/uploads/6938eba830ae9cd28790f5b7/NbUm2nE_sJBo7Nb8IvHTY.png)

## Problem Breakdown & Computational Thinking

why i chose Binary Search

i chose binary search because it is one of the main searching algorithms we learned 
and how it is also more efficient than linear search on sorted lists (O(log n) vs O(n)) and it clearly shows how we can divide and conquer a problem by repeatedly cutting the search space in half.

Decomposition 

i broke the task into these parts

1. input handling by getting a line of text from the user and turn it into a list of integers and get the target value as an integer.
2. Precondition check by making sure the list is already sorted in non-decreasing order.
3. binary search logic becausd i keep track of lower upper and mid and comparing lst[mid] to the target and move either left or right.
Record each step in a list of strings called steps.
4. join all recorded steps into a single string to display for the output and show that string in a textbox n gradio
5. user interface by building a simple Gradio interface with one textbox for the sorted list, one textbox for the target value a button to run the search and a large textbox at the bottom to show the step-by-step process

Pattern Recognition
Each iteration:
 i compute `mid = (lower + upper) // 2` and always compare lst[mid] with the target and if lst[mid] < target, we move the lower index up wheras if lst[mid] > target move the upper index down anbd we keep going until we find the target, or  
  upper < lower (which means the target is not in the list).

Abstraction

to keep the UI simple i am thinking of only using the current values of lower upper and mid and the values in the list at those indices
i'll also add a short explanation of what the algorithm is doing at each step  

if there just so happens to be a bad input,i will show a short error message

Algorithm Design 

1. user types a sorted list of integers separated by spaces and a target integer.
2. convert the text into a list of ints and a target.
3. check that the list is sorted
4. if inputs are valid then we shall run the iterative binary search and record each step in an empty list
5. the function returns the joined steps as one string.



flowchart
start ↓

input: ask for list amd target ↓

check if list is sorted ↓

decision: is input Valid si list sorted?

no → ERROR cuz of invalid Input or Unsorted → end

yes → ↓

is upper >= lower?

no → display ERROR: target isnt found as output → end 

yes → ↓

calculate mid = (lower + upper) // 2 ↓

if list[mid] == target

yes → target found at index mid → End

no → ↓

if list[mid] < target fro right half

yes → lower = mid + 1 to move on the rght of the list

no then target in left half since list[mid] > target so upper = mid - 1 to movr on the lefthand side of the list ↓

Step count +1 

↓
end

## Hugging Face Link: https://huggingface.co/spaces/FirasHussainn/binary-search-firas
## Author: Firas Hussain

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
