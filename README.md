## A http request from the chatgpt api in a discord bot
This repository contains the code for a Discord intelligent automaton. 

### built with

* [Python](https://www.python.org/)
* [Discord.py](https://pypi.org/project/discord.py/)
* [OS](https://pypi.org/project/os/)

# Introduction

This repository contains the "intelligent-discord-bot," a Discord program. This program was created with the intention of providing a simple method for adding artificial intelligence to the user's Discord server.
The program uses the TensorFlow library to train an artificial intelligence machine learning model using data from its Discord server. He can be trained to recognize patterns in messages, such as whether a message is a question or a response.
Additionally, the program can be set up to automatically reply to Discord server messages. The responses are generated using the [markovify] library (https://github.com/jsvine/markovify).

## How to use

You must install the necessary dependencies and clone this repository in order to start using the program.
Additionally, you will need to create a file called config.json in the root of the repository with the following settings:
```
{
  "discord_token": "SEU_TOKEN_DO_DISCORD",
  "owner_id": "SEU_ID_DO_DISCORD",
  "prefix": "!"
}
```
You can obtain your Discord code by visiting this page (https://discordapp.com/developers/applications/me).
To start the program, run the following command:
```python3 main.py```

## IMAGES

<img src="https://dsm04pap002files.storage.live.com/y4m4qQ9yRoFvGqPhS0MW8ohPQmrPFyuxjknFSfrhWmc8JBFmFFz-XBUroPAb9VFuCIBObDxrw1bbXPAkLL-QKNsEDWfQO-p6sKf1SSiS63SNzxcB1Wuoaey8y6vKX4-f9RvC_e0otMHuZ9C077_e-V99JDwFqcu7PSX4GdUHtYtFogcW6e0CTeEqcjrWXdAtG26?width=571&height=180&cropmode=none" width="571" height="180" />
<img src="https://dsm04pap002files.storage.live.com/y4mshR2-V3vSb_7V0WnLXoNCxza6WiopoXvzsMjdQtRf59TAzjaH2k3UvwKVN-JJULF9bQYQ8NopN7uLV39KfVPEKXY8FkCssdTO6j0w8-m7ZgdCEZVevtlnLdiKWDiDmhOjcgp3lbBNT6RtaanBz4QXdzwogHxbt_zbMX7V3Wu1cImT1UWbRAtn9E29BSQ7NZ8?width=660&height=473&cropmode=none" width="660" height="473" />
<img src="https://dsm04pap002files.storage.live.com/y4m8AZR6-T9nHNc4I18gKjnPgIiyXietsoZq_w7xOHyFsX4vO5Aie3D3wQB2i83nIZYjtdRcg3yBRFbz9N2gGlJAAvJ3Z4dF3eG6I5y1F1Yb1sKMKJSxdyZJqkvkaJmzm-14aNfvlMS3_Fk3RevRQm7PMLLc9PHczL0aW7EupHgVcCQHkQxEUiCCa4pEg0nysdt?width=660&height=425&cropmode=none" width="660" height="425" />

## Commands

The program has the following commands:

-!train: Begin the machine learning model's training procedure.
!predict: Make a prediction about the specified message.
-!respond: Enable or disable the bot's automatic response.
-!help: Displays a collection of commands.

### installation

1. clone the repo
   ```sh
   git clone https://github.com/CarllosHenrique/Intelligent-discord-bot.git
   ```
2. install dependencies
   ```sh
   python3 main.py
   ``` 
## contributing
1. fork the project
2. create your feature branch 
```sh
git checkout -b feature/AmazingFeature
```
3. commit your changes
```sh
git commit -m 'Add some AmazingFeature'
```
4. push to the branch 
```sh
git push origin feature/AmazingFeature
```
5. open a pull request
