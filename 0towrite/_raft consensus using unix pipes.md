Raft consensus using unix pipes
=== 

what is raft?
---
Raft is a consensus algorithm.

what is a consensus algorithm?
---
In distributed computing, there is a common problem of different nodes agreeing on values.
This is important to do useful work in a distributed system as if we dont agree on the state of these systems they risk going out of sync and losing sensibility (they start acting like n different systems instead of n systems acting together to solve a problem).
A consensus algorithm allows different nodes of a distributed system to agree on their state even if some nodes fail.  

what does state look like? 
--- 
Lets say a single systems state can be modelled as a state machine, what we have a in a distributed system, is a replicated state machine. 

how do replicated state machines work?
--- 
Replicated state machines use replicated logs to ensure that state machines execute the same commands in the same order. 
The consensus algorithm is responsible for proper log replication. 
Raft is not byzantine fault tolerant i.e. it does not work properly if one of the nodes is a bad actor.  

![replicated state machine][0]

what makes raft unique
--- 
The core design goal of raft was understandability, the researchers argues that Paxos (which was the industry standard before raft) is a correct algorithm but too hard to wrap one's head around.
Raft is not trivial but its simpler to understand than paxos, it also thinks of consensus of multiple values by default instead of single value consensus of paxos.
This allows all the implementations to be more similar as library authors dont have to make their own mechanisms for multivalue consensus over Paxos, they can just use raft.


what makes this implementation unique?
--- 
Distributed systems are usually distributed over the network by default which means using tcp. 
This raft implementation is purely academic and is only ever be going to run on one node, this gives us the liberty to use unix pipes instead of tcp.
Unix pipes are way more fun to work with and also demonstrates in a certain way that this code is original.


System Model 
--- 
*Some pre-conditions*   
- all nodes must be co-operative (no bad actors)  
- all nodes must have a similar notion of time (this is due to the random delays that are used)  
- a majority of the nodes must always run  

*components of the system*   
- leader election  
- log replication  
- terms  

Working principle
---

*Randomness*
Raft uses randomness to avoid situations where multiple nodes continuously compete to become the leader at the same time. Each node starts a *randomized election timeout*. If a node doesn’t hear from a leader before its timeout expires, it assumes the leader has failed and starts an election by becoming a *candidate*.
The randomness ensures that not all nodes start an election simultaneously, which reduces the chance of repeated vote conflicts and helps the system converge quickly to a single leader.

*Leader Election*
Leader election is the mechanism by which Raft ensures that at most one node acts as the *leader* at any given time. The leader is responsible for handling all client requests and coordinating log replication.
1. Nodes begin in the *follower* state.  
2. If a follower does not hear from a leader within its election timeout, it becomes a *candidate* and requests votes from other nodes.   
3. Other nodes will vote for the first candidate they receive a request from in that term.  
4. If a candidate receives votes from a *majority* of nodes, it becomes the leader.  
5. The leader then sends periodic *heartbeats* to maintain authority and prevent new elections.  

This process guarantees that even if nodes fail or messages are delayed, a leader will eventually be elected as long as a majority of nodes are alive.

*Log Replication*
Raft uses *replicated logs* to make sure all nodes apply the same sequence of commands to their state machines. Once a leader is elected:
1. The leader receives client commands and appends them to its log.
2. It sends these log entries to all followers in *AppendEntries* RPCs (or, in your Unix pipe version, messages through the pipe).
3. Followers append the entries to their logs and acknowledge back to the leader.
4. Once a log entry is replicated on a *majority* of nodes, it is considered *committed*, and the leader applies it to its state machine.
5. Followers eventually apply the committed entries to their own state machines, ensuring all nodes stay in sync.

This way, Raft maintains a consistent, fault-tolerant replicated state machine even if some nodes crash.


*Terms*
Raft organizes time into *terms*, which are sequential numbers representing periods of leadership. Terms serve multiple purposes:
1. *Election safety*: Nodes only vote once per term, preventing multiple leaders in the same term.
2. *Log consistency*: If a candidate has outdated logs, it can be rejected by nodes with newer logs.
3. *Failure recovery*: When a new leader is elected in a new term, it helps synchronize the logs across nodes.
Each term starts with an election and may end when a leader is elected. Leaders and followers keep track of the current term to coordinate voting and log replication.


References:
---
1. [Author's talk ][ref1]  
1. [Raft original paper][ref2]  
1. [Terraform's raft implementation in go][ref3]  
1. [UUIC Conference talk on Raft][ref4]  
1. [Raft visualization tool][ref5]

[ref1]: https://www.youtube.com/watch?v=vYp4LYbnnW8
[ref2]: https://raft.github.io/raft.pdf
[ref3]: https://github.com/hashicorp/raft/blob/main/raft.go
[ref4]: https://raft.github.io/slides/uiuc2016.pdf
[ref5]: https://raft.github.io/

[0]: ./state_machine.png
