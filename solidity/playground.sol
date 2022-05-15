//SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.7.0 <0.9.0;


contract playgroundContract{

    int private age = 50;

    address private _contractOwner;
    uint public constant MAX_MINT_NUMBER = 10;
    uint256 public constant price = 30000000000000000;
    bool public isMintLive = true;

    uint public currentMintIdx;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier ownerFunction() {
        require(_contractOwner == msg.sender, "Not allowed to run this function");
        _;
    }

    constructor (){
        address msgSender = msg.sender;
        _contractOwner = msgSender;
        emit OwnershipTransferred(address(0), msgSender);
    }

    function greeting(string memory _firstName, string memory _lastName) public pure returns(string memory){
        return string(abi.encodePacked("Hello ", _firstName, " ", _lastName));
    }

    function testFunction(int _num1, int _num2) public pure returns(int){
        int _sum = _num1 + _num2;
        return _sum;
    }

    function getPersonVote() public view returns(bool){
        bool _canVote = age > 18;
        return _canVote;
    }

    function _getVotePower() private view returns(int){
        int _votePower = int(age / 10);
        if(_votePower > 10){
            _votePower = 10;
        }
        return _votePower;
    }

    function getRandom(uint _max) public view returns(uint){
        uint rand = uint(keccak256(abi.encodePacked(block.timestamp)));
        return rand % _max;
    }

    function getCallerAddress() public view returns(address){
        return msg.sender;
    }

    function transferFund(address payable _address, uint _amount) public {
        _address.transfer(_amount);
    }

    function owner() public view returns(address){
        return _contractOwner;
    }

    function toggleMint() public ownerFunction {
        isMintLive = !isMintLive;
    }

    function checkCurrentMintIdx() public view returns(uint){
        return currentMintIdx;
    }

    function _updateCurrentMintIdx() public payable{
        currentMintIdx += 1;
    }

    function mintToken(uint amount) public payable {
        require(isMintLive, "Minting is not allowed right now");
        require(msg.value >= (price * amount), "Incorrect eth");

        uint mintIdx;
        for(uint i=0; i < amount; i++){
            mintIdx = currentMintIdx;
            if(mintIdx < MAX_MINT_NUMBER){
                // mint token here
            }
            else{
                toggleMint();
            }
            _updateCurrentMintIdx();
        }
    }
}







