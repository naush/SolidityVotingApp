pragma solidity ^0.4.2;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Voting.sol";

contract TestVoting {
  bytes32[] candidateNames;

  function testValidCandidate() {
    candidateNames.push("Rama");
    Voting instance = new Voting(candidateNames);
    Assert.equal(true, instance.validCandidate("Rama"), "Candidate name should be valid");
  }

  function testTotalVotesForCandidate() {
    candidateNames.push("Rama");
    Voting instance = new Voting(candidateNames);
    uint expected = 0;
    Assert.equal(expected, instance.totalVotesFor("Rama"), "Total votes for a new candidate should be zero");
  }

  function testVoteForCandidate() {
    candidateNames.push("Rama");
    Voting instance = new Voting(candidateNames);

    instance.voteForCandidate("Rama");

    uint expected = 1;
    Assert.equal(expected, instance.totalVotesFor("Rama"), "Total votes for a new candidate should be zero");
  }
}

