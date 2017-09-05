pragma solidity ^0.4.11;

import "truffle/Assert.sol";
import "../contracts/Voting.sol";

contract TestVoting {
  bytes32[] candidateNames;
  Voting machine;

  function beforeAll() {
    candidateNames.push("Fabrice");
    machine = new Voting(candidateNames);
  }

  function testCandidatesAreAdded() {
    Assert.equal("Fabrice", machine.candidateList(0), "First candidate should be Fabrice");
  }

  function testValidCandidateIsTrue() {
    Assert.isTrue(machine.validCandidate("Fabrice"), "Fabrice should be valid");
  }

  function testTotalVotesForCandidate() {
    uint8 totalVotes = machine.totalVotesFor("Fabrice");
    Assert.isTrue(totalVotes == 0, "Total votes should be zero for a new candidate");

    machine.voteForCandidate("Fabrice");
    totalVotes = machine.totalVotesFor("Fabrice");

    Assert.isTrue(totalVotes == 1, "Total votes should be one after one vote");
  }

  function testVoteForInvalidCandidate() {
    Assert.isFalse(machine.validCandidate("Alexandre"), "Alexandre should be invalid");
  }
}
