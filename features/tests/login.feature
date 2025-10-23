Feature: User can login to account

  Scenario: From login page user can login with proper creds
    Given User navigates to login page
    Then User inputs email
    And User inputs password
    When User clicks continue button
    Then Home screen is presented

