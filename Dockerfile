FROM python:3.12-slim

RUN apt update  && apt-get upgrade -y && apt install -y --no-install-recommends \
    default-jre \
    git \
    ssh \
    zsh \
    curl \
    wget \
    fonts-powerline \
    && apt-get clean



RUN useradd -ms /bin/bash python

RUN pip install pdm

USER python

WORKDIR /home/python/app

COPY . /home/python/app



ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" \
    -t https://github.com/romkatv/powerlevel10k \
    -p git \
    -p git-flow \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting \
    -a 'export TERM=xterm-256color' \
    -a 'CASE_SENSITIVE="true"'

RUN echo "[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh" >> ~/.zshrc && \
    echo "HISTFILE=/home/python/zsh/.zsh_history" >> ~/.zshrc && \
    echo 'eval "$(pdm --pep582)"' >> ~/.zshrc && \
    echo 'eval "$(pdm --pep582)"' >> ~/.bashrc



CMD [ "tail","-f","/dev/null" ]
