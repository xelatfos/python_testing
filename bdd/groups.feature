Scenario: Add a new group
  Given a group list
  When I add a new group
  Then group list len = len+1