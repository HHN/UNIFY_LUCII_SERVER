<p align="center">
  <a href="https://www.hs-heilbronn.de/de/induko" target="blank"><img src="induko_image.png" width="600" alt="Induko Logo" /></a>
</p>

[circleci-image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token=abc123def456
[circleci-url]: https://circleci.com/gh/nestjs/nest

<p align="center">

Heilbronn University is researching advanced technical tools and didactic approaches designed to foster collaboration and interaction. The primary goal is to enhance and facilitate interdisciplinary, inter-faculty, and inter-university cooperation. Through the InduKo research project, we aim to strengthen this collaboration using innovative digital tools and modern, digitally supported strategies that boost motivation and foster innovation through partnership.

Academic institutions are full of untapped collaboration potential. Researchers, faculty, students, alumni, and industry partners often have complementary interests but struggle to find the right connections. Lucii helps bridge this gap by enabling targeted networking, whether for research projects, study groups, mentoring, or industry collaboration. Lucii is a specialized matching solution designed to connect individuals in academic environments based on shared interests, expertise, and collaboration potential. Built on the Matrix messaging protocol and powered by AI on Edge, Lucii enables privacy-preserving matchmaking and initial anonymous contact without requiring a centralized database or external data processing. All profile evaluations and interest matching take place locally on the user’s device, ensuring that no sensitive profile information is stored on central servers.

Lucii showcases how AI on Edge and the Matrix protocol can bring together the right people in a privacy-preserving way. By combining decentralized messaging with local AI-based matchmaking, Lucii demonstrates how meaningful academic connections can be established without the need for central processing and storage of highly personal profile information.

<a href="https://www.hs-heilbronn.de/en/projekt-induko-2cab68e84c21b797" target="_blank">InduKo</a> Project was funded by  <a href="https://stiftung-hochschullehre.de/en/" target="_blank">Stiftung Innovation in der Hochschullehre</a> (August 2021 - July 2024).

</p>

# Lucii Server
Matrix Dendrite & Anonymous Matching Bot

Lucii Server enables decentralized anonymous messaging and matchmaking with:

Matrix Dendrite – A lightweight homeserver for secure, encrypted messaging.

Python Matrix Bot – Manages anonymous research matching and chat room creation.


Key Features

AI-Powered Anonymous Matchmaking – Users are connected based on research interests while remaining anonymous.

Decentralized Messaging – All communications are end-to-end encrypted via Matrix Dendrite.

Automated Chat Room Management – The bot creates and moderates secure discussion spaces.

No Centralized Storage – All interactions remain private, with no central database storing messages.



---


## Getting Started

Prerequisites

Before setting up the Lucii Server, ensure you have:

Python 3.8+ installed

Matrix Dendrite Server (see Matrix Dendrite Docs)

Flask and nio-matrix installed


Installation & Setup

1. Clone the Repository:

git clone <Lucii-server-repo-link>
cd Lucii-server


2. Install Dependencies:

pip install -r requirements.txt


3. Configure the Bot in config.json:

{
    "matrix_server": "https://matrix.lucii.com",
    "bot_username": "@bot_user:matrix.lucii.com",
    "bot_password": "securepassword",
    "all_user_ids": ["@userA:matrix.lucii.com", "@userB:matrix.lucii.com"]
}


4. Run the Lucii Bot:

python bot.py




---

Bot Usage

Commands

Register Research Interests:

!register AI, NLP, Federated Learning

Find Matches:

!findmatch

Create an Event:

{
  "name": "AI Ethics Panel",
  "details": "Discussion on AI and privacy",
  "keywords": ["AI", "Privacy"],
  "creator": "@userA:matrix.lucii.com",
  "is_group": true
}

Reply Anonymously:

reply:event_12345: I'm interested in discussing AI ethics!



---





## License
- This project is licensed under [Apache 2.0](LICENSE). Copyright 2024 , Hochschule Heilbronn.

## Acknowledgments

This project was developed as part of the **InduKo Project**, funded by **Stiftung Innovation in der Hochschullehre**. We also acknowledge the support from students, faculty, and contributors who have been part of this collaborative effort.

For more information about the InduKo research project, visit the official website.
