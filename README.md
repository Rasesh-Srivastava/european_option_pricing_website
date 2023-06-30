# Website to calculate the price of European Options
Built using Django, HTML and CSS.

## Features

Option to calculate the price using:
- Two-Step Binomial Tree method
-  n-Step Binomial Tree method
-  Black-Scholes Model

## Deployed Website

- [European Options Price Calculator Website Link](https://europeanoptionpricing.onrender.com)\
  **Note**: Since I have deployed the Website on Render using the Free plan of Render, so the website will work and load slowly.\
  **Note**: This link will not open the website if the website has exceeded the Free Usage Limitations of Render, since it will get suspended by Render.

  If this link to the deployed website does not work, then please refer to the screenshots below / run the website locally.

## Screenshots:-
![WhatsApp Image 2023-03-30 at 3 55 00 PM](https://user-images.githubusercontent.com/116264587/228808483-cb8679af-17cf-4bf9-9ad4-acae0a24cf2c.jpeg)

![WhatsApp Image 2023-03-30 at 3 55 24 PM](https://user-images.githubusercontent.com/116264587/228808584-2b22d8dd-cfbb-45ae-a3b2-46a510781a8c.jpeg)

![WhatsApp Image 2023-03-30 at 3 56 23 PM](https://user-images.githubusercontent.com/116264587/228808628-e0471b15-be19-44c7-885f-23c114759d2d.jpeg)

![WhatsApp Image 2023-03-30 at 3 57 04 PM](https://user-images.githubusercontent.com/116264587/228808663-667c1c61-2653-4e9d-844a-81ec2714a931.jpeg)

## Steps to run the website:-
- Clone this GitHub Repo in your local computer.
- Open Terminal. From the root directory of this project, i.e., from the OptionPricing folder, run the command:

  ```bash
  python manage.py runserver
  ```
- If there is any error and link for the local server is not generated, then first run the command:
  
  ```bash
  python manage.py migrate
  ```
  and then, run the command:
  
  ```bash
  python manage.py runserver
  ```
- Open the link generated in the terminal to view the European Option Pricing Website.

## Tech Stack

- Back-End : Django
- Front-End : HTML, CSS

## FeedBack

If you have any suggestions or feedback, please reach out to me at rasesh220303@gmail.com

