module Main where

import Lib

main :: IO ()
main = print (multiples [1 .. 999])

-- Project Euler
-- #1
multiples :: [Int] -> Int
multiples [] = 0
multiples (x:xs) = if mod x 3 == 0 || mod x 5 == 0 then x + multiples xs else multiples xs--or x : multiples xs

--sum :: Foldable t => t a -> Int 



--sum = 0
--for i in range(1000):
--	if i % 3 == 0 or i % 5 == 0:
--		sum += 1

--def sum_multiples(x):
--	if x == 3:
--		return 3
--	elif x == 5:
--		return 5
--	elif x % 3 == 0 or x % 5 == 0:
--		return x + sum_multiples(x - 1)
--	else:
--		return sum_multiples(x - 1)




--def fib(n):
--	if n <= 3:
--		return n
--	else:
--		return fib(n - 2) + fib(n - 1)

--def sum_fib(x):
--	def generate_next(x):
--		return x + 2
--	if n == 1:
--		return n
--	else:
--		sum = 0
--		while fib(n) < 4000000:
--			sum += fib(x) + fib(x+2)


-- Answer should be 2633 = 950 (all the multiples of 5 < 100) + 1683 (all the multiples of 3 < 100)




-- Useful Stack Commands
-- stack build : downloads anything needed but missing to build your project
-- stack --help: stack guide
-- ~/.stack : go into the stack root directory
-- ./.stack-work : go into the local project directory
-- stack --version : discover what version of stack you have
-- stack new : create a new project (contains Haskell package of the same name)
  -- use with new-teplate to use a project template
    -- e.g. ~$ stack new helloworld new-template  --> creates a project in the helloworld directory
-- stack setup : manually check and install whatever packages you are missing for your project
-- stack exec : run the executable
-- stack test : builds the test suite if not already and then runs it automatically
-- stack path : path information (later)
-- stack exec -- which ghc : see where GHC is installed
-- stack --resolver lts-11.22 build : downloads lts-11.22 build plan, changes resolvers
-- stack --resolver nightly : use the newest Nightly resolver available
-- stack --resolver lts : use the newest LTS
-- stack --resolver lts-2 : use the newest LTS in the 2.X series

---------------------------------------------------------------------------------------------------------------------------------------------------

-- Files
  -- stack.yaml : blueprint in root directory of project; contains reference called resolver to the snapshot your package will be built against
    -- extra-deps : defines extra dependencies not present in the resolver
      -- e.g. extra-deps:
      --      - acme-missiles-0.3
    -- leans toward LTS vs. Nightly
  -- library
  -- executable
  -- Haskell source files for our project functionality
    -- app/Main.hs
    -- src/Lib.hs
    -- test/Spec.hs
  -- LICENSE
  -- README.md
  -- helloworld.cabal (don't modify! - automatically created during stack build process)
  -- Of interest
    -- Setup.hs #component of Cabal build system
    -- stack.yaml #project-level settings
      -- fields include packages (tells stack which local packages to build) and resolver (how to build your package)
    -- package.yaml #the preferred package format used to generate the .cabal file
      -- Added packages (under dependecies): text, filepath, containers, acme-missiles
      -- Note: Some packages are not part of the LTS (Long Term Support) package set. Need to add manually using extra-deps in stack.yaml.

-- Note: stack is built on top of the Cabal build system. In Cabal, there are individual packages, each of which contains
-- a single .cabal file. The .cabal file defines >= 1 components: a library, executables, test suites, benchmarks, etc.
-- Also specifies additional info like library dependecies, default language pragmas, etc.

---------------------------------------------------------------------------------------------------------------------------------------------------

-- Stack Vocabulary
-- package
-- project
-- cabal
-- GHC
-- resolver
-- snapshot
-- reproducible builds