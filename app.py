import gradio as gr

def is_sorted_non_decreasing(nums):
    #this wll check that the list is sorted in ascending (non-decreasing) order since it must be sorted as it is binary search!
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True



def binary_search_steps(lst, target):
 
    steps = [] #make empty lisit to keep trsck of step count

    lower = 0
    upper = len(lst) - 1
    count = 1

    while upper >= lower:
        mid = (upper + lower) // 2

        #show state of variables for each step
        steps.append(
            f"step {count}: lower={lower} (value {lst[lower]}), "
            f"upper={upper} (value {lst[upper]}), "
            f"mid index={mid} (value {lst[mid]})"
        )

        #when target vsalue is found
        if lst[mid] == target:
            steps.append(f"{target} has been FOUND at index {mid}.")
            return mid, steps

        #we move right on the list when value is less than target value
        if lst[mid] < target:
            steps.append(
                f"{lst[mid]} < {target} lower = mid + 1. "
                f"checks for a higher index to find target value"
            )
            lower = mid + 1
        else:
            #move left too check the lefthand side fo the list
            steps.append(
                f"{lst[mid]} > {target} upper = mid - 1 "
                f"checks for a lower index to find target value."
            )
            upper = mid - 1

        steps.append("")  # spacing
        steps.append("")
        count += 1

    #when its not found
    steps.append(
        f"ERROR: Your entered target value of {target} "
        f"does not exist in the given list."
    )
    return None, steps


def run_binary_search(list_text, target_text):
    try:
        lst = [int(x) for x in list_text.split()]
    except ValueError: #if user types letters or comma then stop and show an error
        return "ERROR: list should only have whole numbers separated by spaces and no commas."
    try:
        target = int(target_text.strip())
    except ValueError: #if they type something weird we tell the user
        return "ERROR: target must be a single whole number."
    if not is_sorted_non_decreasing(lst): #we ned to make sure that the list is always sorted
        return "ERROR: the list must be sorted in non-decreasing (ascending) order."
    index, steps = binary_search_steps(lst, target)
    return "\n".join(steps)


#interface
with gr.Blocks() as demo:
    gr.Markdown("# Binary Search: By Firas ")

    gr.Markdown(
        """###  
What is Binary Search?

Binary search is a simple searching algorithm that works only on sorted lists.  
It finds a target value by repeatedly:
1. Checking the middle element,
2. Deciding whether the target is in the left or right half,
3. Then discarding the other half.

Because the search space gets cut in half each step, the algorithm is very fast and 
its time complexity ends up being O(log n)

The implementation of this code can be found below:
```python
def binary_search(lst, target):
    lower = 0
    upper = len(lst) - 1

    while upper >= lower:
        mid = (lower + upper) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1

    return None
    ```
        """
            )

    with gr.Row():
        list_input = gr.Textbox(  
            label="Enter a Sorted list seperated by spaces (ex 10 24 46 53 67 120 158 228 250 301 400)",
            lines=2,
            placeholder="10 24 46 53 67 120 158 228 250 301 400",
        )
        target_input = gr.Textbox(
            label="Target value (ex 67)",
            lines=1,
            placeholder="67",
        )

    run_button = gr.Button("Search") #button to run search 

    output_box = gr.Textbox( #add big textbox at the bottom
        label="Binary Search Step by step process",
        lines=24,
    )

    run_button.click( #literallu just the button
        fn=run_binary_search,
        inputs=[list_input, target_input],
        outputs=output_box,
    )


if __name__ == "__main__":
    demo.launch()
