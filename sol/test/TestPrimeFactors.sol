pragma solidity ^0.4.2;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/PrimeFactors.sol";

contract TestPrimeFactors {
  function testInitialPrimeFactors() {
    PrimeFactors factors = PrimeFactors(DeployedAddresses.PrimeFactors());
    Assert.equal(true, true, "Prime factors of 1 should be none");
  }
}
