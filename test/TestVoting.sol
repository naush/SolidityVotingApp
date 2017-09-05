pragma solidity ^0.4.2;

import "truffle/Assert.sol";
import "../contracts/Voting.sol";

contract TestVoting {
  bytes32[] candidateNames;
  Voting machine;

  function beforeAll() {
    candidateNames.push("Rama");
    machine = new Voting(candidateNames);
  }

  function testCandidatesAreAdded() {
    bytes32 candidateName = machine.candidateList(0);
    Assert.equal("Rama", candidateName, "Candidate names are added to list");
  }

  function testValidCandidateIsTrue() {
    Assert.isTrue(machine.validCandidate("Rama"), "Candidate name should be valid");
  }

  function testTotalVotesForCandidate() {
    uint expected = 0;
    Assert.equal(expected, machine.totalVotesFor("Rama"), "Total votes for a new candidate should be zero");
  }

  function testVoteForCandidate() {
    machine.voteForCandidate("Rama");

    uint expected = 1;
    Assert.equal(expected, machine.totalVotesFor("Rama"), "Total votes for a new candidate should be one");
  }

  function testVoteForInvalidCandidate() {
    machine.voteForCandidate("John");

    uint expected = 0;
    Assert.equal(expected, machine.totalVotesFor("John"), "Total votes for a new candidate should be zero");
  }
}
