Feature: User can click on topics in the side menu

  Scenario: User can filter the off plan products by Unit price range
    Given User navigates to login page
    Then Complete login
    Then Home screen is presented
    Then User clicks off-plan in side menu
    And User verifies they are on Off-plan page
    When User clicks the Price filter
    Then User inputs the 1200000 and 2000000
    Then User clicks the apply filter button
    Then User verifies all visible property prices are within range 1200000 and 2000000

