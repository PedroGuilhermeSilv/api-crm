FROM python:3.11-slim

RUN apt update -y && apt-get upgrade -y && apt install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install pdm

WORKDIR /home/python/app

COPY . /home/python/app
RUN chmod +x /home/python/app/commands-prod.sh

ENV MY_PYTHON_PACKAGES=/home/python/app/.venv


RUN echo "[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh" >> ~/.zshrc && \
    echo "HISTFILE=/home/python/zsh/.zsh_history" >> ~/.zshrc && \
    echo 'eval "$(pdm --pep582)"' >> ~/.zshrc && \
    echo 'eval "$(pdm --pep582)"' >> ~/.bashrc && \
    pdm install

EXPOSE 5003

CMD ["/home/python/app/commands-prod.sh"]