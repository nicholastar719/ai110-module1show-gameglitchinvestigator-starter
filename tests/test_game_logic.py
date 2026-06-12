from pathlib import Path
from logic_utils import check_guess
from streamlit.testing.v1 import AppTest

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# FIX: Regression test added with AI assistance — AI generated this AppTest to verify the Enter-key form submission bug is resolved
def test_form_submit_processes_guess():
    """
    Regression test for the Enter-key bug.
    Before the fix, the submit used st.button (click-only).
    Now it uses st.form_submit_button, which responds to both
    click and Enter. This test verifies that submitting via the
    form actually increments attempts (i.e., the guess is processed).
    """
    app_path = Path(__file__).parent.parent / "app.py"
    at = AppTest.from_file(str(app_path))
    at.run()

    attempts_before = at.session_state["attempts"]

    at.text_input[0].set_value("42")
    at.form_submit_button[0].click()
    at.run()

    assert at.session_state["attempts"] == attempts_before + 1
