```toml
title = "2nd Order Effects of Claude"
tags = ["ai,","software practices"] 
date = 2026-04-20
```

Here are some of the second order benifits I've seen due to the rise of claude code (and other ai agents) -

### Tooling 

- Claude code made me discover git worktrees.
- Re-discovered ripgrep and started using it.

### Behaviour

- Context: Claude does not have the entire repo in its context at once, it fires a few grep queries and gets enough context to do simple tasks. I have started doing the same exept I have much more than 1M context.
- Planning Phase: I've learnt to do planning in the same way claude does before doing a big task. This is obvious to some, but still worth mentioning.
- Spawning Subagents: If an llm model can spawn subagents pretending to be a staff engineer/security researcher/critiquer I can do the same. I now read code wearing different hats to see if I can find some bugs. This means reading code at different levels of abstraction and with different concerns.

### Documentation

- People now have claude.md files which are great for giving claude context of the repo. They are also great at giving me context of the repo. Don't have to talk to anyone to get context.
- Agents love code comments and I do too, more codebases have them now.

