FROM pytorch/pytorch

WORKDIR "/workspace"
RUN apt-get clean \
        && apt-get update \
        && apt-get install -y ffmpeg libportaudio2 openssh-server python3-pyqt5 xauth gcc build-essential\
        && apt-get -y autoremove \
        && mkdir /var/run/sshd \
        && mkdir /root/.ssh \
        && chmod 700 /root/.ssh \
        && echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config \
        && echo "X11Forwarding yes" >> /etc/ssh/sshd_config \
        && echo "PermitRootLogin yes" >> /etc/ssh/sshd_config \
        && echo "X11UseLocalhost yes" >> /etc/ssh/sshd_config
RUN echo "root:root" | chpasswd
ADD Multi-Language-RTVC/requirements.txt /workspace
RUN pip install -r requirements.txt
RUN echo "export PATH=/opt/conda/bin:$PATH" >> /root/.profile
ENTRYPOINT ["sh", "-c", "/usr/sbin/sshd && bash"]
CMD ["bash"]