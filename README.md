*****
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sveneschlbeck/Multi-Language-RTVC)
![GitHub top language](https://img.shields.io/github/languages/top/sveneschlbeck/Multi-Language-RTVC)
![GitHub](https://img.shields.io/github/issues/sveneschlbeck/Multi-Language-RTVC)
![GitHub](https://img.shields.io/github/issues-pr/sveneschlbeck/Multi-Language-RTVC?color=orange)
![GitHub](https://img.shields.io/github/stars/sveneschlbeck/Multi-Language-RTVC?style=social)
![GitHub](https://img.shields.io/github/forks/sveneschlbeck/Multi-Language-RTVC?style=social)
![GitHub](https://img.shields.io/github/repo-size/sveneschlbeck/Multi-Language-RTVC)
![GitHub](https://img.shields.io/tokei/lines/github/sveneschlbeck/Multi-Language-RTVC)
![GitHub](https://img.shields.io/github/contributors/sveneschlbeck/Multi-Language-RTVC)
![GitHub](https://img.shields.io/badge/Since-2021-brightgreen)
![GitHub](https://img.shields.io/badge/License-MIT-brown.svg)
![GitHub](https://img.shields.io/github/workflow/status/sveneschlbeck/Multi-Language-RTVC/Lint)
![GitHub](https://img.shields.io/badge/code%20style-black-black)
*****

![MLRTVC logo](img/MLRTVC_readme.png)

``Multi-Language-RTVC`` stands for Multi-Language Real Time Voice Cloning and is a Voice Cloning Tool capable
of transfering speaker-specific audio features to synthesize speeches in that voice based on just a few
seconds of unknown audio data.

## Installation & Setup
In order for ``MLRTVC`` to work, you need Python installed on your machine. Visit https://www.python.org/downloads/ and download
Python for your Operating System (OS).  
In addition to core Python, some dependant packages are required. They can be found [here](environment.yml).

For more information on...

...how to install ``Python``,  
...how to create a virtual environment using ``Anaconda``,  
...how to clone a repository using ``Git``,  
...how to setup ``CUDA``,
...how to install ``PyTorch`` and
...how to get started with ``MLRTVC``  

for both ``Windows`` and ``Linux``, visit our [Installation & Setup Wiki](https://github.com/sveneschlbeck/Multi-Language-RTVC/wiki/Installation-&-Setup).

## Using Docker

**Make sure you have docker and nvidia-container-toolkit installed**

```
## To install nvidia-container-toolkit

# For ubuntu
sudo apt install -y nvidia-docker2

# For arch linux
yay -S nvidia-container-toolkit
```

### Set up SSH config on the host machine

#### NOTE: you need to set X11Forwarding to yes in /etc/ssh/sshd_config on the docker host as well and 
Add the following to your SSH config at `~/.ssh/config` on the docker host (or create the file if it doesn’t exists):

```
Host voice
    Hostname localhost
    Port 2150
    User root
    ForwardX11 yes
    ForwardX11Trusted yes
```


**Keep the Dockerfile outside the main directory like below**

![tree structure](https://user-images.githubusercontent.com/6279035/147375101-4b2df8fe-8d83-4c7f-bd91-7db60ded0abc.png)

**Build the docker image**

```
docker build -t racoon-bse . 
```

**Run the Docker Container**

```
docker run -it --rm --init --gpus=all \
        --privileged \
        -e DISPLAY=${DISPLAY} \
        --ipc=host --volume="$PWD:/workspace" \
        -e NVIDIA_VISIBLE_DEVICES=0 -p 2150:22 \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        --device /dev/snd racoon-bse
```

**Keep the docker run tab open, and use a new window for the steps below**

**Allow the connection to the X server**

```
xhost + 
```

**SSH inside the container**

Default username and password is root
```
ssh -X voice
```

**Run the apps as usual**

```
export DISPLAY=:0

cd /workspace/Multi-Language-RTVC/mlrtvc/src
python mlrtvc_toolbox.py
```

---

## License

This code is licensed under ``MIT``. For more information regarding the license model or
associated duties and rights, click [here](LICENSE.md).

## Ethics & Legal

With the exception of one's own voice, the cloning of voices may only be done with the voices of people
who have expressly consented to the use of their voice for AI applications or whose statements,
speeches or recordings are publicly available and not protected by copyright.  
``MLRTVC`` gives users the power and the potential to create statements that were never made in this form
and thus represent fictions. This power binds the users of this software to the duty to use this technology
responsibly, to always think about the consequences of their actions and to use cloning exclusively in the
course of curiosity, science and learning.  
If synthetically generated statements are used to blackmail other people, influence political debates or
deliberately spread false statements in the real or digital world, this can lead to negative consequences
for people and severe legal penalties.  
We as developers and the ``MLRTVC`` community assume no liability or
responsibility for the use of ``MLRTVC`` by others and will strictly refuse to cooperate with people who
have negative intentions regarding the use of voice cloning.

## Project History

This project was started in 2021 with the goal of inheriting Corentin Jemine's [``Real-Time-Voice-Cloning``](https://github.com/CorentinJ/Real-Time-Voice-Cloning).
The project originated from the wish of multi-language support for voice cloning models and is now
maintained and enhanced by contributing volunteers. Visit the [``About us``](https://github.com/sveneschlbeck/Multi-Language-RTVC/wiki/About-us) section to learn more about the team behind ``MLRTVC``.

## Contributing

We welcome all those interested in the project, from beginners to experts. The MLRTVC community standard is
a nice, open-minded and efficient working climate. We encourage all those with ideas to take part in the
project by sharing their thoughts.  
There are multiple meaningful ways of contributing:

- Developing code (new features, fixes, enhancements)
- Writing documentation and Wiki entries
- Raising issues (bugs, feature requests, enhancement proposals, code refacturing, etc.)
- Providing pre-trained models
- Participating in community tasks (code reviews, discussions, maintenance, etc.)

For transparacy reasons, we ask you to engage with this project via the official ways (issues, pull requests)
to share knowledge and questions publicly. Only in cases where privacy or confidentiality is of great importance,
other communication channels are accepted (email, chat, etc.).

Further information can be gained in the [``Contributing Guidelines``](CONTRIBUTING.md).

## Code of Conduct

Working together on this project, we share and defend certain values which are indispensable
for an Open Source project like ``MLRTVC``. For further information see [here](https://github.com/sveneschlbeck/Multi-Language-RTVC/blob/main/CODE_OF_CONDUCT.md).

## Help & Support

### Documentation

- About us: https://github.com/sveneschlbeck/Multi-Language-RTVC/wiki/About-us
- FAQ: https://github.com/sveneschlbeck/Multi-Language-RTVC/wiki/Frequently-Asked-Questions-(FAQ)
- Repository Structure: https://github.com/sveneschlbeck/Multi-Language-RTVC/wiki/Repository-Structure
- Theory behind ``MLRTVC``: https://github.com/sveneschlbeck/Multi-Language-RTVC/wiki/Theory
- Upcoming Events: https://github.com/sveneschlbeck/Multi-Language-RTVC/wiki/Upcoming-Events  

### Communication

- Stack Overflow: https://stackoverflow.com/questions/tagged/mlrtvc
- GitHub Discussions: https://github.com/sveneschlbeck/Multi-Language-RTVC/discussions
- Discord: https://discord.gg/asym7axdgd

### Citation

If you use this software in your own work, software implementations or research, please cite by navigating to the ``Cite this repository`` dropdown menu
in the right sidebar and choose your citation style.

![Citing](img/citing.png)
