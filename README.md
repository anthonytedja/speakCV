# SpeakCV

[![Preview](assets/img/thumbnail.jpg)](https://anthonytedja.github.io/speakCV/)

> SpeakCV is a desktop client that automates video call actions through your webcam.

## Setup

Visit our [website](https://anthonytedja.github.io/speakCV/) and click the download button to download the zip file containing SpeakCV.

### Installing Python

You will need [Python](https://www.python.org/downloads) (> version 3.9.12). To check whether it's already installed on a UNIX-like system, open up a terminal window (e.g. Terminal on OS X) and type `python --version` at the command prompt. For example, you should see something similar to the following:

```bash
$ python --version
Python 3.9.12
```

### Installing OBS

Ensure you have [OBS](https://obsproject.com/download) installed on your PC to ensure that you can use your webcam in Zoom while using SpeakCV.

### Installing Anaconda

You will need  [Anaconda](https://www.anaconda.com/) in order to install the necessary dependencies SpeakCV relies on to function properly.

### Installing Dependencies

Create the environment from the `environment.yml` file:

```bash
conda env create -f environment.yml
```

Activate the new environment:

```bash
conda activate deerhack
```

## Documentation

### :speech_balloon: The Motive

Throughout our Zoom university journey, our team has noticed that we often forget to unmute our mics when we talk, or forget to mute it when we don't want others to listen in. To combat this problem, we created a desktop client SPEAKCV, that uses computer vision to understand when you are talking and will automatically mute and unmute your mic for you.

### :hammer: The Team

[@anthonytedja](https://github.com/anthonytedja)  
[@raghavst](https://github.com/raghavst)
[@kevshinXP](https://github.com/kevshinXP)  
[@hani64](https://github.com/hani64)  

### :wrench: How We Built It

We used Dlib's HOG-based face detector to map out landmark point on a users face. We used a pre-existing model to extract 68 landmark coordinates which map to contours on a users face. These landmark points can be used to map a users facial features such as there eyebrows, eyes, nose, jaw, and mouth.

For SpeakCV we are interested in the 19 landmark points used to map out a users mouth. We used these 19 landmark points to calculate the aspect ratio of a user's mouth at any given time. We determined that if the aspect ratio of a users if above a certain threshold, we can reasonably assume that user is speaking. If a user speaking is detected, SpeakCV unmutes a user during their zoom call. When the user closes there mouth again SpeakCV mutes the user back.

We used Tkinter to create a user-friendly interface that can be used to launch SpeakCV. The interface gives the user the option to see a debug window which shows the detected facial feature in real time using the power of OpenCV. The interface also allows the user to change the default mute delay from 5 seconds to whatever suits them.

### :brain: The Takeaways

How to setup and use virtual environments in Anaconda to ensure everyone could work on the code locally without issues. Another thing we learned was to use virtual video/audio to access videos/ audio from our own programs. We also learned a bit about GUI creation for Python applications.

### :star: The Features

- Automatic Zoom muting/unmuting based on user speech
- Customizable mute timeout duration
- Debug mode for developers
