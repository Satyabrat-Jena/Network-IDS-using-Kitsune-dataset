// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PacketLogger {
    struct Packet {
        address sender;
        uint256 timestamp;
        string features; // Store features as a string (JSON or comma-separated)
    }

    Packet[] public packets;

    event PacketLogged(address indexed sender, uint256 timestamp, string features);

    function logPacket(string memory _features) public {
        packets.push(Packet(msg.sender, block.timestamp, _features));
        emit PacketLogged(msg.sender, block.timestamp, _features);
    }

    function getPacketCount() public view returns (uint256) {
        return packets.length;
    }

    function getPacket(uint256 index) public view returns (address, uint256, string memory) {
        require(index < packets.length, "Index out of bounds");
        Packet memory p = packets[index];
        return (p.sender, p.timestamp, p.features);
    }
}