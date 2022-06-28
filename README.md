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

### Register 

- The form indicates the required fields of Username, Email (optional), a password and then to re-enter password to confirm they match.

<img>

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

- :hover and :active pseudo classes were used to change colours on links adding to the User Experience.

## Testing

- I confirmed that the site is responsive on a variety of device sizes through DevTools.

- I confirm that the colours and fonts all contrast and allow the user to easily navigate the site.

- I confirm that multiple users can be signed up to the site.

- I confirm that both the comments and like features function as expected.

- I confirm that the site works in both Safari and Chrome.

## Fixed Bugs

- All Bootstrap classes resolve flow and sizing issues on smaller devices.

- Users cannot submit empty fields on the registration form.

## Unfixed Bugs

- HTML errors from W3C validator that don't affect site functionality.

## Deployment

The site was deployed to Heroku by following these steps:

1. Create a Heroku account, and choose create new app

2. Ensure config vars are set up for app

3. Add buildpack for Python.

4. Deploy the site through choosing Github in the deploy section

5. Click on deployed site link once complete to take you to [ThymeOnTheRoad]()

## Credits

### Content

- All images on the site are the work of Ariel Rose Wright

- All icons on the site are taken from [FontAwesome](https://fontawesome.com/).

- The font used on the site is from [Google Fonts](https://fonts.google.com/).

- The framework used for the recipe site is from the Blog Walkthrough at [Code Institute](https://codeinstitute.net/).

### Media

- The pagination idea is taken from the Code Institute Blog Walkthrough Project.

### Future Development Opportunities

## User Focused

- A form could be added so that users can submit their own recipes for adding to the site with admin approval.

- The site could have further sections for types of cuisine, time taken to cook recipes so users could make a simpler journey round the site to choose what/how they want to cook.

- Videos could be added to each recipe of the cooking method.

- Clicking on the "Recipes from time spent travelling and cooking" could link to an "About" section with info about the site oweners.

## Developer Focused

- Automated tests could be written and used to test site functionality.

### Thanks

- My wife for being my UX companion for the site and for helping test it for me, as well as providing the artwork.

- My mentor Chris for his feedback and encouragement throughout the project.
