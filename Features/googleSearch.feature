Feature: Search
  Scenario: Verify google search
    Given user is on google search page
    And enters text to search
    Then Relavent results are displayed
    When user executes the following query
    """
    select * from {db_name}.emp
    where name='sampath'
    """
    Then difference is 3