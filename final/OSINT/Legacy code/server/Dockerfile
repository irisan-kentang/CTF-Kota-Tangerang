FROM k3gabut4ndev/bot-kegabutan:latest

WORKDIR /bot-kegabutan

USER root
ADD src/bot.py src

RUN chown -R root:root /bot-kegabutan
RUN chmod +x /bot-kegabutan/src/bot.py

USER nobody
CMD /bot-kegabutan/src/bot.py
