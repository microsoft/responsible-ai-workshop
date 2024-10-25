# Responsible AI Workshop - Cloning the repo 

For most of its modules, not to say all, the workshop contains hands-on tutorials/walthroughs that come with different guide(s) and presentation(s) if any.  

Various options are available to clone this repo. For the sake of this workshop, we assume here that you have a Windows 10 (or above) local environment with possibly [Windows Subsystem for Linux (WSL) 2 installed](https://learn.microsoft.com/en-us/windows/wsl/install) with an Ubuntu distribution. (This also de facto covers both Linux and MacOS environment). Let’s consider them in order. 

Let’s start with Git for Windows.  

## Cloning the repo using Git for Windows 

To clone the repo on your Windows 10 local machine, perform the following steps: 

1. Download the [Git for Windows](https://github.com/git-for-windows/git/releases/download/v2.25.0.windows.1/Git-2.25.0-64-bit.exe) and run it. 

2. In the pop-up window, click **Install**. Follow the instructions. 

3. Open a PowerShell console, and run the following command: 

```  
PS C:\> md rai-workshop 

PS C:\> cd C:\rai-workshop\ 

PS C:\> git clone https://github.com/microsoft/responsible-ai-workshop.git 

```

## Cloning the repo using Git on Ubuntu 

Likewise, to clone the repo on your Ubuntu environment (WSL2), from a Bash terminal console, run the following commands: 

```
$ cd $home 

$ mkdir rai-workshop 

$ cd rai-workshop 

$ git clone https://github.com/microsoft/responsible-ai-workshop.git 
```

You can instead install GitHub for Desktop for Windows.  

## Cloning the repo using GitHub Desktop 

To clone the repo on your Windows 10 local machine, perform the following steps: 

1. Download the [GitHub Desktop](https://central.github.com/deployments/desktop/desktop/latest/win32) installer and run it. 

2. In the pop-up window, click **Install**. Follow the instructions. 

3. Open a browser session and navigate on GitHub to the main page of [the Responsible AI Workshop repo ](https://github.com/microsoft/responsible-ai-workshop). 

4. Click **Clone** or **download**. 

5. Click **Open in Desktop** to clone the repository. GitHub Desktop opens up and a dialog shows up. 

6. Click **Choose**... and, using Windows Explorer, navigate to a local path where you want to clone that repo. Throughout this guide, we will use the rai-workshop folder as an illustration. 

7. Click **Clone**. 

See [Cloning a repository from GitHub to GitHub Desktop](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop). 

 

