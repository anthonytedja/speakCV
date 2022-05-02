# SpeakCV

[![Preview](assets/img/thumbnail.jpg)](https://anthonytedja.github.io/speakCV/)

> SpeakCV is a desktop client that automates video call actions with OpenCV.

## Setup

Visit our [website](https://anthonytedja.github.io/speakCV/) and click the download button to get the zip file containing SpeakCV. (you will only need the speech_code folder), or get the speech_code folder directly from this repository.

![Download](assets/img/download.jpg)

### Zoom Settings

Under the Audio Section, make sure to enable mute your microphone when joining a meeting or SpeakCV. will work in the opposite way.

![Mute](assets/img/mute.jpg)

Under the Keyboard Shortcuts Section, make sure to enable the global shortcut for Mute/Unmute My Audio, and have the shortcut as Alt+A to ensure SpeakCV. will work in the background.

![Shortcut](assets/img/shortcut.jpg)

### Installing OBS

Ensure you have [OBS](https://obsproject.com/download) installed on your PC to use your webcam in Zoom with SpeakCV.

### Installing Anaconda

You will need  [Anaconda](https://www.anaconda.com/) in order to install the necessary dependencies for SpeakCV.

After installing Anaconda, open up Anaconda Powershell Prompt / Anaconda Prompt for the following commands.

You will need Python 3.9.12+ for SpeakCV. Check your current python version in the terminal with `python --version`

```bash
$ python --version
Python 3.9.12
```

Use the following command to install the correct version if your python version is not above 3.9.12:

```bash
conda install python=3.9.12
```

Create the environment from the `environment.yaml` file to install the dependencies:

```bash
conda env create -f environment.yaml
```

## Usage

Activate the environment:

```bash
conda activate deerhack
```

Run the GUI:

```bash
python gui.py
```

Now you're all set to use SpeakCV. alongside Zoom!

## Documentation

### :speech_balloon: Inspiration

Throughout our Zoom university journey, our team noticed that we often forget to unmute our mics when we talk, or forget to mute it when we don't want others to listen in. To combat this problem, we created SpeakCV, a desktop client that automatically mutes and unmutes your mic for you using computer vision to understand when you are talking.

### :wrench: How We Built It

We used Dlib's HOG-based face detector to map out landmark point on a users face. We used a pre-existing model to extract 68 landmark coordinates which map to contours on a users face. These landmark points can be used to map a users facial features such as there eyebrows, eyes, nose, jaw, and mouth.

![Dots](assets/img/dots.png)

For SpeakCV we are interested in the 19 landmark points used to map out a users mouth. We used these 19 landmark points to calculate the aspect ratio of a user's mouth at any given time. We determined that if the aspect ratio of a users if above a certain threshold, we can reasonably assume that user is speaking. If a user speaking is detected, SpeakCV unmutes a user during their zoom call. When the user closes there mouth again SpeakCV mutes the user back.

We used Tkinter to create a user-friendly interface that can be used to launch SpeakCV. The interface gives the user the option to see a debug window which shows the detected facial feature in real time using the power of OpenCV. The interface also allows the user to change the default mute delay from 5 seconds to whatever suits them.

### :star: The Features

- Automatic Zoom muting/unmuting based on user speech
- Customizable mute timeout duration
- Debug mode for developers

### :brain: What we learned

How to setup and use virtual environments in Anaconda to ensure everyone could work on the code locally without issues. Another thing we learned was to use virtual video/audio to access videos/ audio from our own programs. We also learned a bit about GUI creation for Python applications.

### :heart: What's next

Improve the precision of the shape recognition model, either by further adjusting the mouth aspect ratio or by tweaking the contour spots used in the algorithm for determining mouth shape. Moving the application to the Zoom app marketplace by making the application using the Zoom SDK, which requires migrating the application to C++. We can also instead use the Zoom API and move the application onto the web.

### :hammer: The Team

[@anthonytedja](https://github.com/anthonytedja)

[@raghavst](https://github.com/raghavst)

[@kevshinXP](https://github.com/kevshinXP)

[@hani64](https://github.com/hani64)
