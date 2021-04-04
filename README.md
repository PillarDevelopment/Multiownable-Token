# Multiownable-Token

1) Two owner addresses transmit the parameters new and previous owners sequentially
```
TransferOwnership(address, address)
```

2) Two owner addresses transmit the parameters sequentially
```
mint(address, uint256)
```

3) Two owner addresses transmit the parameters sequentially
```
burn(address, uint256)
```

4) Two owner addresses transmit the parameters from - allOperations[allOperationsCount-1]
```
canselPending(bytes32)
```

5) get max available emission
```
MaxSupply()
```

6) get operation bytes32 HASH by index 
```
allOperations[uint256]
```

7) get totalOperations length
```
allOperationCount()
```

8) get operation index by hash
```
allOperationsIndicies[bytes32]
```

9) get necessary signers
```
howManyOwnersDecide()
```

10) get owner address by index
```
owners[uint256]
```

11) get owner index by address
```
ownersIndices[address]
```

