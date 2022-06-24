# ThymeOnTheRoad

## Thyme On The Road Website

This is the main website for the recipe site Thyme On The Road. This website was inspired by mine and my wife's travels, and our cooking whilst we were on our adventures. Cooking in a hostel, tent or camper van doesn't have to be boring or unhealthy!

<img>

## User Experience

### User Stories

### First time user goals

- First time users should be able to easily navigate the site and view the content on any device.

- First time users should be able to view recipes, and follow the methods to cook them for themselves.

- First time users should be able to sign up to the site and create an account.

- First time users should be able to follow the social media links to find out more about the website owners and it's legitimacy.

### Returning user goals:

- As a returning user I want to be able to like and comment on recipes.

### Frequent user goals:

- I would like to see regular new recipes from the admin team.

- I want to see only comments that are appropriate for a recipe website.

## Design

### Colour scheme:

The main colours used are pastel shades of orange, green, red and brown. THese are coupled with a beige that serves as the light background for much of the site. It gives the site a more organic feel than clinical bright colours. I found the pallet for this at [ColorsWall] (https://colorswall.com/palette/31431).

### Fonts/Typography:

The main font used across the whole site is Merienda. It fits well with the colour scheme, and again, is less clinical than some more modern looking typefaces. It's fallback font is Sans Serif.

### Images:

Being a recipe website, images of the food are important. However, as lots of the recipes were created "on the road", it wasn't always possible to take good photos of them. Instead, I have chosen to use artists (my wifes) interpretations of what the food looked like. 

## Wireframes/Sketches

<img>

## Features

- Responsive on a variety of devices.

- Regularly updated content.

- Commenting and liking features for signed up users.

- Admin features for the site oweners to approve comments, and add content.

### Header/Navigation

- Logo/site title is in the top left of the screen. Pressing on it will link you back to the top of the homepage.

- To the right of the bar is the remaining navigation links. Home, Register and Login. Once the user is logged in, this changes to Home and Logout. On smaller devices, the navbar drops down to a hamburger menu for better user experience on mobile. 

- The background colour, and the font colours chosen stand out well making it easy for the user to see where they are and what they are doing.

- The navigation makes it clear to the user what can be accessed on the site.

<img>

### Recipes

- The recipes load 6 to a page, with pagination to allow users to move to "next" and "previous" pages once 6 has been reached.

### Footer

- This links the user to the 4 main social media accounts for the community.

- This allows them to confirm the legitimacy of the site, whilst also joining the social media followings.

- The footer colours mirror the header, with the FontAwesome icons changing colour when hovered over to indicate to the user that they can be pressed. They also change to a different colour to show the user when they have been active.

<img>

### Register *******

- The form indicates the 4 required fields for first and last names, location, email and preferred item to swap.

- The colours contrast to allow the user to easily navigate the form.

- The "Let's Get Swapping" button changes colour when hovered over, again indicating to the user that it can be pushed.

<img width="990" alt="Form" src="https://user-images.githubusercontent.com/92179145/143723555-5c9c9871-517a-49a7-b88b-d97f071996ba.png">

## Technology used

### Languages used

- HTML 5 

- CSS

- Python 3.8

- Django

- Bootstrap 4

### Frameworks, libraries and programs used:

- Google Fonts. Both main fonts used throughout the site are from the [Google Fonts](https://fonts.google.com/) repository.

- Font Awesome. All icons used through the site are imported from the directory at [FontAwesome](https://fontawesome.com/).

- [GitHub](https://github.com/) was used to host the repositories and for site deployment.

- [GitPod](https://gitpod.io/) was used for all writing of code.

- hover.css. Hover.css was used to change colour when hovering over the icons and nav titles.

- PhotoShop was used to alter the image used in the Locations section.

- [Pexels](https://www.pexels.com/) was used for all of the imagery on the site.

## Testing

- I confirmed that the site is responsive on a variety of device sizes through DevTools.

- I confirm that the colours and fonts all contrast and allow the user to easily navigate the site.

- I have confirmed that the form cannot be submitted without a valid email and without all fields being filled in, but the join button does not link to anywhere due to the site address not being live.

- I confirm that the site works in both Safari and Chrome.

## Validation

- I confirm that no errors were found when passing it through the W3C html validator.

- I confirm that no errors were found when passing through the Jigsaw CSS validator.

- I confirm that the site is easy to read and navigate by passing it through the Lighthouse tool on DevTools.

<img width="990" alt="Accessibility" src="https://user-images.githubusercontent.com/92179145/143723766-3fcd3b10-5716-42b8-85c2-267968783df7.png">

## Fixed Bugs 

- After running the W3C html validator, I converted the Philosophy and Locations headings to h2 from h1 to avoid issues in the CSS styling of the code. 

- I removed an ALotToSwap logo from the header bar as it was causing issues with image sizing in the Pictures section, as well as being pushed from the page altogether when the size of the screen was shrunk beyond a certain point.

- All media queries resolved size and flow issues on smaller devices.

## Unfixed Bugs

- The nav menu is displayed in the wrong order when the site is displayed on smaller screen sizes.

- The social media icons in the footer are not perfectly centred on smaller screens.

- One picture disappears from the pictures gallery at 470px and below.

## Deployment

The site was deployed to GitHub pages by following these steps:

1. In the GitHub repository, find the Settings tab.

2. From the Source section drop down menu select "Main".

3. Press "Refresh".

4. GitHub then creates the live link for the site.

It can also be found at [ALotToSwap](https://bernardlerring.github.io/ALotToSwap/).

## Credits

### Content

- All images on the site are taken from [Pexels](https://www.pexels.com/).

- All icons on the site are taken from [FontAwesome](https://fontawesome.com/).

- Both fonts used on the site are from [Google Fonts](https://fonts.google.com/).

### Media

- The code used for the Join Us form and the Social Media links was taken from the CI Love Running walkthrough project and modified to suit the style of the ALotToSwap site.

- The idea for the masonry style photo layout on the Pictures page and the hero image animation were inspired by the CI Love Running walkthrough project.

### Personal Development

- I am aware that h1 headings should not be used beyond the very first heading as brought up as a warning in my W3C validation of my index.html file. If I was to change them to h2 headings at this late stage, I would have to change all h2 headings to h3 and so on, along with all their associated CSS stylings.  

- It would appear that through reaching out on the Slack channel, that there was an issue with GitHub that caused a grafted git history to appear on my repository around the time I was editing some of my code and my ReadMe.MD. 

- In future, I will also use Balsamiq for my wireframes as I am aware that pencil drawings do not look as proffessional or as detailed as could be.

### Thanks

- Dave H from the Slack Community for helping me sort out my issues with GitHub.

- My Partner for being my UX companion for the site and for helping test it for me.

- My mentor for his feedback and encouragement throughout the project.
