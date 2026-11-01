# Setup guide (Windows)

Work through this once. It takes 30–45 minutes. If a step doesn't work, stop
and write down the exact error message. Error messages are useful.

---

## 1. Install Python

1. Go to <https://www.python.org/downloads/> and download the latest Python 3 installer.
2. Run it. **On the first screen, tick "Add python.exe to PATH".**
   If you miss this, nothing below will work.
3. Click "Install Now".

**Check:** open **PowerShell** (Start menu → type "PowerShell") and type:

```bash
python --version
```

You should see something like `Python 3.13.x`. Any version from 3.12 up is fine.

If the Microsoft Store opens instead, the PATH box wasn't ticked. Run the
installer again, choose "Modify", and tick it.

## 2. Install VS Code

Download it from <https://code.visualstudio.com/> and install.

Open VS Code, click the Extensions icon in the left sidebar (four squares),
search for **Python** (the one by Microsoft), and install it.

VS Code is to Python what the VBA editor (Alt+F11) is to Excel, except it
lives outside Excel.

## 3. Install Git

Download from <https://git-scm.com/download/win> and run the installer.
The defaults are fine, with one exception: on the screen
"Choosing the default editor used by Git", pick **Visual Studio Code**.

**Check** (in a *new* PowerShell window):

```bash
git --version
```

Then tell Git who you are. Use the email address you'll use for GitHub:

```bash
git config --global user.name "Jen Yoursurname"
git config --global user.email "you@example.com"
```

## 4. Make a GitHub account

1. Sign up at <https://github.com/signup>.
2. Turn on two-factor authentication (Settings → Password and authentication).
   GitHub requires it anyway.
3. Send Lars your username. He'll invite you to the course repository.
4. Accept the invitation, either from the email or at <https://github.com/notifications>.

## 5. Get the course onto your computer

In VS Code, press **Ctrl+Shift+P**, type **Git: Clone**, and paste the
repository URL Lars gives you. Pick a folder, for example `Documents`.
Sign in to GitHub when asked. When VS Code asks, open the cloned folder.

Now switch to the lesson 00 branch. Open the terminal (**Terminal → New
Terminal**) and run:

```bash
git checkout lesson-00
```

Bottom left in VS Code it should now say `lesson-00` instead of `main`.
You only see the `lessons` folder after this step.

## 6. Start lesson 00

Every lesson lives in its own folder, and you always work *inside* it:

```bash
cd lessons/00-setup
```

Open `GUIDE.pdf` in that folder. That's where the story starts.
Then work through `EXERCISES.pdf`, with `CHEATSHEET.pdf` next to you.
