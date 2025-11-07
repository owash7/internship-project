Feature: Settings info and elements function correctly

  Scenario: User clicks settings and "My clients" verification
    Given User navigates to login page
    Then Complete login
    Then Click settings button
    And Click My clients button
    Then Verify correct page opened
    Then Verify the option amount on the page is 7

    Scenario: Verify options amount on the settings page
      Given User navigates to login page
      Then Complete login
      Then Click settings button
      Then Verify settings page opened
      And Verify the amount of options is 19
      And Verify connect the company button is available


