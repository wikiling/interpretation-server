{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE PatternSynonyms #-}

module Compiler.Tree.Syntax (
  T.Tree(..), TreePosition, T.fromList, T.printTree,
  Label(..), ConstituencyLabel(..), ConstituencyTree(..)
) where

import GHC.Generics
import qualified Data.Tree.Binary.Preorder as T

type TreePosition = String
type Category = String
type Lexeme = String

data Label
  = CatLabel Category
  | LexLabel Lexeme deriving (Show, Generic)

data ConstituencyLabel = CLabel Label TreePosition deriving (Show, Generic)

type ConstituencyTree = T.Tree ConstituencyLabel
