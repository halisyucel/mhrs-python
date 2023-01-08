# Created by halis at 8.01.2023

Feature: Initialize hospital
  This appointment system is for one hospital only.
  Therefore, hospital information must be created before all other endpoints.

  Scenario: Save hospital information
    Given I am a authorized user
    When I send a POST request to "/hospital/initialize" with:
      | name | address | phone | email | website | description |
      | Test Hospital | Test Address | 123456789 |