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

The AI initially gave a partially wrong fix mixing up which hint message belonged to each branch of the if statment. I verified the issue by running the game again and learning that higher guesses gave the wrong direction hint before correcting the logic and retesting it again.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

By running the program again to see if the previous error was gone and instead the program ran as it's expected to.

- Describe at least one test you ran (manual or using pytest)  and what it showed you about your code.

I submitted different guesses while playing the game and instead of pressing the "submit guess" button, I pressed enter and it worked every time.

- Did AI help you design or understand any tests? How?

Yes, any problem I identified it explained to me what part of the code, or what part that isn't in the code, is causing the issue and then in implemented it yourself.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
