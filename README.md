# traveler_software_engineering

Group Members:
 1) Charles Thomas
 2) Omoremi Adeleke
 3) Tania Ortiz-Rosales
 4) Redeat Kibebew

Feature: Index Page
As an authenticated user of the web site traveler
So that I can determine what country and city I may want to visit next
I want a list of all the locations from the Location Table in the home page index
Route: / or index → views.index function → index.html

Feature: Dashboard page
As an authenticated user of the web site
I want to have a page dashboard.html that shows
So that  I can
Route:  /dashboard or dashboard → views.dashboard function → dashboard.html

Feature: Show a Destination
As an authenticated user of the web site traveler
I want a destination to be displayed with all of its features
So that I can see the location, interesting features, and other descriptions about a destination.
Route: show → views.show_destination → show_destination.html

Feature: Show a Location
As an authenticated user of the website traveler
So that I can read all the possible destinations of one location
I want to list all the attributes of a particular location
Route: location/<int:location_id>/show or show_location → views.show_location function → show_location.html

# source djangoenv/Scripts/activate
