Feature: User can navigate home screen

  Scenario: Logged in user can access home screen
    Given User navigates to login page
    Then Complete login
    Then Home screen is presented
