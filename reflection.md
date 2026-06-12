# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| Press Enter | Submit guess/search | Nothing | None |
| Make guess (higher/lower) | Correct hint direction | Hint is the opposite of what it's supposed to be | None |
| Start game again | Same attempt limit | First game has 7 attempts, rest have 8 | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One correct AI suggestion was identifying that the Enter key issue was caused by not using a Streamlit form, and recommending me to wrap the input and submit it in st.form with st.form_submit_button. I verified this by testing the app after the changes were made and confirming that pressing Enter submits the guess instead of not doing anything.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI initially gave a partially wrong fix mixing up which hint message belonged to each branch of the if statement. I verified the issue by running the game again and learning that higher guesses gave the wrong direction hint before correcting the logic and retesting it again.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

By running the program again to see if the previous error was gone and instead the program ran as it's expected to.

- Describe at least one test you ran (manual or using pytest)  and what it showed you about your code.

I submitted different guesses while playing the game and instead of pressing the "submit guess" button, I pressed enter and it worked every time.

- Did AI help you design or understand any tests? How?

Yes, AI helped explain which part of the code was causing the issue and suggested how to implement tests.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script every time you interact with the app. Session state is used to store values so they persist between reruns instead of resetting. Without it, game variables like score or attempts would restart constantly.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I want to reuse the habit of testing changes with pytest before relying on the UI. Next time, I would break AI changes into smaller steps and test more frequently. This project showed me that AI code still needs careful checking and validation instead of trusting it blindly.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I would break AI suggestions into smaller steps and test each change before moving on. This would help catch mistakes earlier instead of fixing multiple issues at once.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project showed me that AI generated code can speed things up, but it still needs to be reviewed and testing because it can introduce small errors.
