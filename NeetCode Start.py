import os

# Categories and problems
categories = {
    "1. Array": [
    "1. Score of a String.py",
    "2. Concatenation of Array.py",
    "3. Contains Duplicate.py",
    "4. Valid Anagram.py",
    "5. Replace Elements With Greatest Element On Right Side.py",
    "6. Is Subsequence.py",
    "7. Append Characters to String to Make Subsequence.py",
    "8. Length of Last Word.py",
    "9. Number of Senior Citizens.py",
    "10. Two Sum.py",
    "11. Longest Common Prefix.py",
    "12. String Matching in an Array.py",
    "13. Group Anagrams.py",
    "14. Pascals Triangle.py",
    "15. Remove Element.py",
    "16. Unique Email Addresses.py",
    "17. Isomorphic Strings.py",
    "18. Can Place Flowers.py",
    "19. Majority Element.py",
    "20. Next Greater Element I.py",
    "21. Longest Strictly Increasing or Strictly Decreasing Subarray.py",
    "22. Maximum Ascending Subarray Sum.py",
    "23. Find Pivot Index.py",
    "24. Kth Distinct String in an Array.py",
    "25. Range Sum Query - Immutable.py",
    "26. Find All Numbers Disappeared in An Array.py",
    "27. Find Missing and Repeated Values.py",
    "28. Maximum Number of Balloons.py",
    "29. Word Pattern.py",
    "30. Design HashSet.py",
    "31. Design HashMap.py",
    "32. Height Checker.py",
    "33. Special Array I.py",
    "34. Check if Array Is Sorted and Rotated.py",
    "35. Monotonic Array.py",
    "36. Divide Array Into Equal Pairs.py",
    "37. Number of Good Pairs.py",
    "38. Pascal's Triangle II.py",
    "39. Find Words That Can Be Formed by Characters.py",
    "40. Count the Number of Consistent Strings.py",
    "41. Largest 3-Same-Digit Number in String.py",
    "42. Destination City.py",
    "43. Maximum Product Difference Between Two.py",
    "44. Circular Sentence.py",
    "45. Maximum Score After Splitting a String.py",
    "46. Path Crossing.py",
    "47. Minimum Changes To Make Alternating Binary String.py",
    "48. Redistribute Characters to Make All Strings Equal.py",
    "49. Longest Palindrome.py",
    "50. Largest Substring Between Two Equal Characters.py",
    "51. Set Mismatch.py",
    "52. First Unique Character in a String.py",
    "53. Intersection of Two Arrays.py",
    "54. Find Common Characters.py",
    "55. Number of Students Unable to Eat Lunch.py",
    "56. Time Needed to Buy Tickets.py",
    "57. Special Array with X Elements Greater than or Equal X.py",
    "58. Count Vowel Strings in Ranges.py",
    "59. Average Waiting Time.py",
    "60. Sort an Array.py",
    "61. Sort Colors.py",
    "62. Relative Sort Array.py",
    "63. Sort the People.py",
    "64. Sort Array by Increasing Frequency.py",
    "65. Top K Frequent Elements.py",
    "66. Encode and Decode Strings.py",
    "67. Range Sum Query 2D Immutable.py",
    "68. Product of Array Except Self.py",
    "69. Minimum Number of Operations to Move All Balls to Each Box.py",
    "70. Valid Sudoku.py",
    "71. Longest Consecutive Sequence.py",
    "72. Encode and Decode TinyURL.py",
    "73. Brick Wall.py",
    "74. Best Time to Buy And Sell Stock II.py",
    "75. Majority Element II.py",
    "76. Minimum Index of a Valid Split.py",
    "77. Subarray Sum Equals K.py",
    "78. Subarray Sums Divisible by K.py",
    "79. Make Sum Divisible by P.py",
    "80. Unique Length 3 Palindromic Subsequences.py",
    "81. Number of Sub-arrays With Odd Sum.py",
    "82. Minimum Number of Swaps to Make The String Balanced.py",
    "83. Number of Pairs of Interchangeable Rectangles.py",
    "84. Maximum Product of The Length of Two Palindromic Subsequences.py",
    "85. Grid Game.py",
    "86. Find All Anagrams in a String.py",
    "87. Find The Index of The First Occurrence in a String.py",
    "88. Wiggle Sort.py",
    "89. Largest Number.py",
    "90. Continuous Subarray Sum.py",
    "91. Push Dominoes.py",
    "92. Repeated DNA Sequences.py",
    "93. Insert Delete Get Random O(1).py",
    "94. Check if a String Contains all Binary Codes of Size K.py",
    "95. Non Decreasing Array.py",
    "96. Number of Ways to Split Array.py",
    "97. Sign of An Array.py",
    "98. Find the Difference of Two Arrays.py",
    "99. Uncommon Words from Two Sentences.py",
    "100. Design Parking System.py",
    "101. Shifting Letters II.py",
    "102. Number of Zero-Filled Subarrays.py",
    "103. Word Subsets.py",
    "104. Optimal Partition of String.py",
    "105. Design Underground System.py",
    "106. Minimum Penalty for a Shop.py",
    "107. Champagne Tower.py",
    "108. Sum of Absolute Differences in a Sorted Array.py",
    "109. Design a Food Rating System.py",
    "110. Convert an Array Into a 2D Array With Conditions.py",
    "111. Minimum Numbers of Operations to Make Array Empty.py",
    "112. Divide Array Into Arrays With Max Difference.py",
    "113. Sequential Digits.py",
    "114. Sort Characters By Frequency.py",
    "115. Sort the Jumbled Numbers.py",
    "116. Find Polygon with the Largest Perimeter.py",
    "117. Minimum Remove to Make Valid Parentheses.py",
    "118. Contiguous Array.py",
    "119. Count Number of Bad Pairs.py",
    "120. Find All Duplicates in an Array.py",
    "121. Find the Length of the Longest Common Prefix.py",
    "122. Count Unguarded Cells in the Grid.py",
    "123. Text Justification.py",
    "124. Naming a Company.py",
    "125. Number of Submatrices that Sum to Target.py",
    "126. First Missing Positive.py",
    "127. Shortest Palindrome.py"
],

    "2. Two Pointer": [
    "1. Reverse String.py",
    "2. Valid Palindrome.py",
    "3. Valid Palindrome II.py",
    "4. Valid Word Abbreviation.py",
    "5. Minimum Difference Between Highest And Lowest of K Scores.py",
    "6. Merge Strings Alternately.py",
    "7. Merge Sorted Array.py",
    "8. Merge Two 2D Arrays by Summing Values.py",
    "9. Move Zeroes.py",
    "10. Remove Duplicates From Sorted Array.py",
    "11. Assign Cookies.py",
    "12. Find First Palindromic String in the Array.py",
    "13. Sort Array by Parity.py",
    "14. Reverse Words in a String III.py",
    "15. Backspace String Compare.py",
    "16. Check If Two String Arrays are Equivalent.py",
    "17. Apply Operations to an Array.py",
    "18. Adding Spaces to a String.py",
    "19. Remove Duplicates From Sorted Array II.py",
    "20. Partition Array According to Given Pivot.py",
    "21. Two Sum II Input Array Is Sorted.py",
    "22. 3Sum.py",
    "23. 4Sum.py",
    "24. Rotate Array.py",
    "25. Container With Most Water.py",
    "26. Number of Subsequences That Satisfy The Given Sum Condition.py",
    "27. Array With Elements Not Equal to Average of Neighbors.py",
    "28. Divide Players Into Teams of Equal Skill.py",
    "29. Boats to Save People.py",
    "30. K-th Symbol in Grammar.py",
    "31. Minimum Time To Make Rope Colorful.py",
    "32. Rearrange Array Elements by Sign.py",
    "33. Bag of Tokens.py",
    "34. Minimum Length of String after Deleting Similar Ends.py",
    "35. Sentence Similarity III.py",
    "36. Trapping Rain Water.py"
],
    "3. Sliding Window": [
        "1. Contains Duplicate II.py",
        "2. Best Time to Buy And Sell Stock.py",
        "3. Minimum Recolors to Get K Consecutive Black Blocks.py",
        "4. Number of Sub Arrays of Size K and Avg Greater than or Equal to Threshold.py",
        "5. Grumpy Bookstore Owner.py",
        "6. Alternating Groups II.py",
        "7. Longest Substring Without Repeating Characters.py",
        "8. Longest Repeating Character Replacement.py",
        "9. Permutation In String.py",
        "10. Frequency of The Most Frequent Element.py",
        "11. Fruits into Basket.py",
        "12. Maximum Number of Vowels in a Substring of Given Length.py",
        "13. Minimum Number of Flips to Make The Binary String Alternating.py",
        "14. Defuse the Bomb.py",
        "15. Minimum Size Subarray Sum.py",
        "16. Find K Closest Elements.py",
        "17. Minimum Operations to Reduce X to Zero.py",
        "18. Get Equal Substrings Within Budget.py",
        "19. Number of Substrings Containing All Three Characters.py",
        "20. Binary Subarrays with Sum.py",
        "21. Count Number of Nice Subarrays.py",
        "22. Subarray Product Less Than K.py",
        "23. Find the Power of K-Size Subarrays I.py",
        "24. Maximum Sum of Distinct Subarrays With Length K.py",
        "25. Length of Longest Subarray With at Most K Frequency.py",
        "26. Count Subarrays Where Max Element Appears at Least K Times.py",
        "27. Maximum Beauty of an Array After Applying Operation.py",
        "28. Take K of Each Character From Left and Right.py",
        "29. Count of Substrings Containing Every Vowel and K Consonants II.py",
        "30. Minimum Window Substring.py",
        "31. Sliding Window Maximum.py",
        "32. Subarrays with K Different Integers.py",
        "33. Minimum Number of Operations to Make Array Continuous.py",
        "34. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.py",
        "35. Smallest Range Covering Elements from K Lists.py"
    ],
    "4. Stack": [
        "1. Crawler Log Folder.py",
        "2. Baseball Game.py",
        "3. Valid Parentheses.py",
        "4. Implement Stack Using Queues.py",
        "5. Implement Queue using Stacks.py",
        "6. Final Prices With a Special Discount in a Shop.py",
        "7. Make The String Great.py",
        "8. Min Stack.py",
        "9. Evaluate Reverse Polish Notation.py",
        "10. Removing Stars From a String.py",
        "11. Validate Stack Sequences.py",
        "12. Generate Parentheses.py",
        "13. Asteroid Collision.py",
        "14. Daily Temperatures.py",
        "15. Online Stock Span.py",
        "16. Car Fleet.py",
        "17. Simplify Path.py",
        "18. Decode String.py",
        "19. Remove K Digits.py",
        "20. Remove All Adjacent Duplicates In String II.py",
        "21. Reverse Substrings Between Each Pair of Parentheses.py",
        "22. Minimum String Length After Removing Substrings.py",
        "23. Clear Digits.py",
        "24. Minimum Add to Make Parentheses Valid.py",
        "25. Maximum Width Ramp.py",
        "26. 132 Pattern.py",
        "27. Flatten Nested List Iterator.py",
        "28. Sum of Subarray Minimums.py",
        "29. Maximum Frequency Stack.py",
        "30. Robot Collisions.py",
        "31. Largest Rectangle In Histogram.py",
        "32. Shortest Subarray with Sum at Least K.py",
        "33. Parsing A Boolean Expression.py",
        "34. Number of Atoms.py"
    ],
    "5. Binary Search": [
        "1. Binary Search.py",
        "2. Search Insert Position.py",
        "3. Guess Number Higher Or Lower.py",
        "4. Arranging Coins.py",
        "5. Squares of a Sorted Array.py",
        "6. Valid Perfect Square.py",
        "7. Sqrt(x).py",
        "8. Single Element in a Sorted Array.py",
        "9. Find Peak Element.py",
        "10. Successful Pairs of Spells and Potions.py",
        "11. Search a 2D Matrix.py",
        "12. Koko Eating Bananas.py",
        "13. Capacity to Ship Packages Within D Days.py",
        "14. Maximum Candies Allocated to K Children.py",
        "15. House Robber IV.py",
        "16. Minimize the Maximum Difference of Pairs.py",
        "17. Minimized Maximum of Products Distributed to Any Store.py",
        "18. Minimum Limit of Balls in a Bag.py",
        "19. Minimum Time to Repair Cars.py",
        "20. Find Minimum In Rotated Sorted Array.py",
        "21. Search In Rotated Sorted Array.py",
        "22. Search In Rotated Sorted Array II.py",
        "23. Time Based Key Value Store.py",
        "24. Find First And Last Position of Element In Sorted Array.py",
        "25. Maximum Number of Removable Characters.py",
        "26. Populating Next Right Pointers In Each Node.py",
        "27. Most Beautiful Item for Each Query.py",
        "28. Search Suggestions System.py",
        "29. Count the Number of Fair Pairs.py",
        "30. Split Array Largest Sum.py",
        "31. Find K-th Smallest Pair Distance.py",
        "32. Median of Two Sorted Arrays.py",
        "33. Find in Mountain Array.py"
    ],
    "6. Linked List": [
        "1. Reverse Linked List.py",
        "2. Merge Two Sorted Lists.py",
        "3. Linked List Cycle.py",
        "4. Palindrome Linked List.py",
        "5. Remove Linked List Elements.py",
        "6. Remove Duplicates From Sorted List.py",
        "7. Middle of the Linked List.py",
        "8. Intersection of Two Linked Lists.py",
        "9. Merge in Between Linked Lists.py",
        "10. Merge Nodes in Between Zeros.py",
        "11. Find the Minimum and Maximum Number of Nodes Between Critical Points.py",
        "12. Remove Nodes From Linked List.py",
        "13. Reorder List.py",
        "14. Maximum Twin Sum Of A Linked List.py",
        "15. Remove Nth Node From End of List.py",
        "16. Delete Nodes From Linked List Present in Array.py",
        "17. Swapping Nodes in a Linked List.py",
        "18. Copy List With Random Pointer.py",
        "19. Design Linked List.py",
        "20. Design Browser History.py",
        "21. Add Two Numbers.py",
        "22. Find The Duplicate Number.py",
        "23. Swap Nodes In Pairs.py",
        "24. Sort List.py",
        "25. Partition List.py",
        "26. Rotate List.py",
        "27. Reverse Linked List II.py",
        "28. Design Circular Queue.py",
        "29. Insertion Sort List.py",
        "30. Split Linked List in Parts.py",
        "31. LRU Cache.py",
        "32. LFU Cache.py",
        "33. Merge K Sorted Lists.py",
        "34. Reverse Nodes In K Group.py"
    ],
    "7. Trees": [
        "1. Binary Tree Inorder Traversal.py",
        "2. Binary Tree Preorder Traversal.py",
        "3. Binary Tree Postorder Traversal.py",
        "4. N-ary Tree Postorder Traversal.py",
        "5. Invert Binary Tree.py",
        "6. Maximum Depth of Binary Tree.py",
        "7. Diameter of Binary Tree.py",
        "8. Balanced Binary Tree.py",
        "9. Same Tree.py",
        "10. Subtree of Another Tree.py",
        "11. Convert Sorted Array to Binary Search Tree.py",
        "12. Merge Two Binary Trees.py",
        "13. Path Sum.py",
        "14. Range Sum of BST.py",
        "15. Leaf-Similar Trees.py",
        "16. Evaluate Boolean Binary Tree.py",
        "17. Create Binary Tree From Descriptions.py",
        "18. Binary Tree Vertical Order Traversal.py",
        "19. Construct String From Binary Tree.py",
        "20. Lowest Common Ancestor of a Binary Search Tree.py",
        "21. Insert into a Binary Search Tree.py",
        "22. Delete Node in a BST.py",
        "23. Binary Tree Level Order Traversal.py",
        "24. Binary Tree Right Side View.py",
        "25. Reverse Odd Levels of Binary Tree.py",
        "26. Minimum Number of Operations to Sort a Binary Tree by Level.py",
        "27. Kth Largest Sum in a Binary Tree.py",
        "28. Cousins in Binary Tree II.py",
        "29. Minimum Distance between BST Nodes.py",
        "30. Symmetric Tree.py",
        "31. Linked List in Binary Tree.py",
        "32. Minimum Time to Collect All Apples in a Tree.py",
        "33. Binary Tree Zigzag Level Order Traversal.py",
        "34. Construct Quad Tree.py",
        "35. Find Duplicate Subtrees.py",
        "36. Check Completeness of a Binary Tree.py",
        "37. Construct Binary Tree from Inorder and Postorder Traversal.py",
        "38. Maximum Width of Binary Tree.py",
        "39. Time Needed to Inform All Employees.py",
        "40. Count Good Nodes In Binary Tree.py",
        "41. Validate Binary Search Tree.py",
        "42. Kth Smallest Element In a Bst.py",
        "43. Construct Binary Tree From Preorder And Inorder Traversal.py",
        "44. Construct Binary Tree from Preorder and Postorder Traversal.py",
        "45. Unique Binary Search Trees.py",
        "46. Unique Binary Search Trees II.py",
        "47. Number of Good Leaf Nodes Pairs.py",
        "48. Sum Root to Leaf Numbers.py",
        "49. House Robber III.py",
        "50. Flip Equivalent Binary Trees.py",
        "51. Operations On Tree.py",
        "52. All Possible Full Binary Trees.py",
        "53. Find Bottom Left Tree Value.py",
        "54. Trim a Binary Search Tree.py",
        "55. Binary Search Tree Iterator.py",
        "56. Validate Binary Tree Nodes.py",
        "57. Find Largest Value in Tree Row.py",
        "58. Pseudo-Palindromic Paths in a Binary Tree.py",
        "59. Even Odd Tree.py",
        "60. Smallest String Starting From Leaf.py",
        "61. Delete Leaves With a Given Value.py",
        "62. Delete Nodes And Return Forest.py",
        "63. Distribute Coins in Binary Tree.py",
        "64. Convert Bst to Greater Tree.py",
        "65. Step-By-Step Directions From a Binary Tree Node to Another.py",
        "66. Recover a Tree From Preorder Traversal.py",
        "67. Binary Tree Maximum Path Sum.py",
        "68. Serialize And Deserialize Binary Tree.py"
    ],
    "8. Heap/Priority Queue": [  
        "1. Kth Largest Element In a Stream.py",
        "2. Last Stone Weight.py",
        "3. Take Gifts From the Richest Pile.py",
        "4. Final Array State After K Multiplication Operations I.py",
        "5. K Closest Points to Origin.py",
        "6. Kth Largest Element In An Array.py",
        "7. Task Scheduler.py",
        "8. Design Twitter.py",
        "9. Least Number of Unique Integers after K Removal.py",
        "10. Furthest Building You Can Reach.py",
        "11. Minimize Deviation in Array.py",
        "12. Maximum Subsequence Score.py",
        "13. Single Threaded CPU.py",
        "14. Seat Reservation Manager.py",
        "15. Process Tasks Using Servers.py",
        "16. Find The Kth Largest Integer In the Array.py",
        "17. Reorganize String.py",
        "18. Longest Happy String.py",
        "19. Car Pooling.py",
        "20. Range Sum of Sorted Subarray Sums.py",
        "21. Find Median From Data Stream.py",
        "22. Maximum Performance of a Team.py",
        "23. IPO.py",
        "24. Minimum Cost to Hire K Workers.py",
        "25. Number of Flowers in Full Bloom.py",
        "26. Constrained Subsequence Sum.py",
        "27. Find Building Where Alice and Bob Can Meet.py"
    ],
    "9. Backtracking": [
        "1. Sum of All Subsets XOR Total.py",
        "2. Subsets.py",
        "3. Combination Sum.py",
        "4. Combination Sum II.py",
        "5. Combinations.py",
        "6. Permutations.py",
        "7. Subsets II.py",
        "8. Permutations II.py",
        "9. Letter Tile Possibilities.py",
        "10. Word Search.py",
        "11. Palindrome Partitioning.py",
        "12. Restore IP Addresses.py",
        "13. Letter Combinations of a Phone Number.py",
        "14. The k-th Lexicographical String of All Happy Strings of Length n.py",
        "15. Matchsticks to Square.py",
        "16. Splitting a String Into Descending Consecutive Values.py",
        "17. Construct Smallest Number From DI String.py",
        "18. Find Unique Binary String.py",
        "19. Split a String Into the Max Number of Unique Substrings.py",
        "20. Maximum Length of a Concatenated String With Unique Characters.py",
        "21. Partition to K Equal Sum Subsets.py",
        "22. The Number of Beautiful Subsets.py",
        "23. Different Ways to Add Parentheses.py",
        "24. Construct the Lexicographically Largest Valid Sequence.py",
        "25. Count Number of Maximum Bitwise-OR Subsets.py",
        "26. N Queens.py",
        "27. N Queens II.py",
        "28. Maximum Score Words Formed By Letters.py",
        "29. Word Break II.py"
    ],
    "10. Tries": [
        "1. Count Prefix and Suffix Pairs I.py",
        "2. Implement Trie Prefix Tree.py",
        "3. Design Add And Search Words Data Structure.py",
        "4. Counting Words With a Given Prefix.py",
        "5. Remove Sub-Folders from the Filesystem.py",
        "6. Extra Characters in a String.py",
        "7. Word Search II.py",
        "8. Sum of Prefix Scores of Strings.py",
        "9. Count Prefix and Suffix Pairs II.py"
    ],
    "11. Graphs": [
        "1. Island Perimeter.py",
        "2. Verifying An Alien Dictionary.py",
        "3. Find the Town Judge.py",
        "4. Count Servers that Communicate.py",
        "5. Find Champion II.py",
        "6. Number of Islands.py",
        "7. Max Area of Island.py",
        "8. Maximum Number of Fish in a Grid.py",
        "9. Clone Graph.py",
        "10. Walls And Gates.py",
        "11. Rotting Oranges.py",
        "12. Count Sub Islands.py",
        "13. Pacific Atlantic Water Flow.py",
        "14. Surrounded Regions.py",
        "15. Reorder Routes to Make All Paths Lead to The City Zero.py",
        "16. Snakes And Ladders.py",
        "17. Open The Lock.py",
        "18. Find Eventual Safe States.py",
        "19. Course Schedule.py",
        "20. Course Schedule II.py",
        "21. Graph Valid Tree.py",
        "22. Course Schedule IV.py",
        "23. Check if Move Is Legal.py",
        "24. Shortest Bridge.py",
        "25. Shortest Path in Binary Matrix.py",
        "26. Number of Connected Components In An Undirected Graph.py",
        "27. Redundant Connection.py",
        "28. Accounts Merge.py",
        "29. Find Closest Node to Given Two Nodes.py",
        "30. As Far from Land as Possible.py",
        "31. Shortest Path with Alternating Colors.py",
        "32. Minimum Fuel Cost to Report to the Capital.py",
        "33. Minimum Score of a Path Between Two Cities.py",
        "34. Number of Closed Islands.py",
        "35. Number of Enclaves.py",
        "36. Regions Cut By Slashes.py",
        "37. Minimum Number of Vertices to Reach all Nodes.py",
        "38. Is Graph Bipartite.py",
        "39. Count the Number of Complete Components.py",
        "40. Evaluate Division.py",
        "41. Detonate the Maximum Bombs.py",
        "42. Find All Possible Recipes from Given Supplies.py",
        "43. Shortest Distance After Road Addition Queries I.py",
        "44. Minimum Height Trees.py",
        "45. Path with Maximum Gold.py",
        "46. Most Profitable Path in a Tree.py",
        "47. Maximum Number of Points From Grid Queries.py",
        "48. Maximum Number of K-Divisible Components.py",
        "49. Sliding Puzzle.py",
        "50. Largest Color Value in a Directed Graph.py",
        "51. Minimum Number of Days to Eat N Oranges.py",
        "52. Find All People With Secret.py",
        "53. Word Ladder.py",
        "54. Parallel Courses III.py"
    ],
    "12. Advanced Graphs": [
        "1. Path with Minimum Effort.py",
        "2. Network Delay Time.py",
        "3. Reconstruct Itinerary.py",
        "4. Min Cost to Connect All Points.py",
        "5. Path with Maximum Probability.py",
        "6. Find the Safest Path in a Grid.py",
        "7. Swim In Rising Water.py",
        "8. Alien Dictionary.py",
        "9. Trapping Rain Water II.py",
        "10. Minimum Obstacle Removal to Reach Corner.py",
        "11. Minimum Cost to Make at Least One Valid Path in a Grid.py",
        "12. Minimum Time to Visit a Cell In a Grid.py",
        "13. Cheapest Flights Within K Stops.py",
        "14. Find the City With the Smallest Number of Neighbors at a Threshold Distance.py",
        "15. Minimum Cost to Convert String I.py",
        "16. Number of Ways to Arrive at Destination.py",
        "17. Making A Large Island.py",
        "18. Minimum Cost Walk in Weighted Graph.py",
        "19. Number of Good Paths.py",
        "20. Maximum Employees to Be Invited to a Meeting.py",
        "21. Remove Max Number of Edges to Keep Graph Fully Traversable.py",
        "22. Minimum Number of Days to Disconnect Island.py",
        "23. Second Minimum Time to Reach Destination.py",
        "24. Find Minimum Diameter After Merging Two Trees.py",
        "25. Find Critical and Pseudo Critical Edges in Minimum Spanning Tree.py",
        "26. Build a Matrix With Conditions.py",
        "27. Greatest Common Divisor Traversal.py",
        "28. Divide Nodes Into the Maximum Number of Groups.py"
    ],
    "13. 1D Dynamic Programs": [
        "1. Climbing Stairs.py",
        "2. Min Cost Climbing Stairs.py",
        "3. N-th Tribonacci Number.py",
        "4. House Robber.py",
        "5. House Robber II.py",
        "6. Longest Palindromic Substring.py",
        "7. Palindromic Substrings.py",
        "8. Decode Ways.py",
        "9. Coin Change.py",
        "10. Maximum Product Subarray.py",
        "11. Word Break.py",
        "12. Longest Increasing Subsequence.py",
        "13. Partition Equal Subset Sum.py",
        "14. Triangle.py",
        "15. Delete And Earn.py",
        "16. Paint House.py",
        "17. Filling Bookcase Shelves.py",
        "18. Combination Sum IV.py",
        "19. Perfect Squares.py",
        "20. Check if There is a Valid Partition For The Array.py",
        "21. Maximum Subarray Min Product.py",
        "22. Minimum Cost For Tickets.py",
        "23. Integer Break.py",
        "24. Number of Longest Increasing Subsequence.py",
        "25. Stickers to Spell Word.py",
        "26. Uncrossed Lines.py",
        "27. Solving Questions With Brainpower.py",
        "28. Count Ways to Build Good Strings.py",
        "29. Ugly Number II.py",
        "30. New 21 Game.py",
        "31. Best Team with no Conflicts.py",
        "32. Longest String Chain.py",
        "33. Knight Dialer.py",
        "34. Partition Array for Maximum Sum.py",
        "35. Largest Divisible Subset.py",
        "36. Stone Game III.py",
        "37. Concatenated Words.py",
        "38. Maximize Score after N Operations.py",
        "39. Find the Longest Valid Obstacle Course at Each Position.py",
        "40. Minimum Number of Removals to Make Mountain Array.py",
        "41. Count all Valid Pickup and Delivery Options.py",
        "42. Number of Ways to Divide a Long Corridor.py",
        "43. Maximum Sum of 3 Non-Overlapping Subarrays.py",
        "44. Maximum Profit in Job Scheduling.py",
        "45. Student Attendance Record II.py"
    ],
    "14. 2D Dynamic Programs": [
        "1. Unique Paths.py",
        "2. Unique Paths II.py",
        "3. Minimum Path Sum.py",
        "4. Maximum Number of Points with Cost.py",
        "5. Longest Common Subsequence.py",
        "6. Longest Palindromic Subsequence.py",
        "7. Length of Longest Fibonacci Subsequence.py",
        "8. Last Stone Weight II.py",
        "9. Best Time to Buy And Sell Stock With Cooldown.py",
        "10. Coin Change II.py",
        "11. Target Sum.py",
        "12. Interleaving String.py",
        "13. Stone Game.py",
        "14. Stone Game II.py",
        "15. Longest Increasing Path In a Matrix.py",
        "16. Maximal Square.py",
        "17. Count Square Submatrices with All Ones.py",
        "18. Ones and Zeroes.py",
        "19. 2 Keys Keyboard.py",
        "20. Maximum Alternating Subsequence Sum.py",
        "21. Distinct Subsequences.py",
        "22. Edit Distance.py",
        "23. Number of Dice Rolls with Target Sum.py",
        "24. Minimum Falling Path Sum.py",
        "25. Out of Boundary Paths.py",
        "26. Longest Ideal Subsequence.py",
        "27. Count Number of Teams.py",
        "28. Shortest Common Supersequence.py",
        "29. Count Vowels Permutation.py",
        "30. Burst Balloons.py",
        "31. Number of Ways to Rearrange Sticks With K Sticks Visible.py",
        "32. Regular Expression Matching.py",
        "33. Flip String to Monotone Increasing.py",
        "34. Maximum Value of K Coins from Piles.py",
        "35. Number of Music Playlists.py",
        "36. Number of Ways to Form a Target String Given a Dictionary.py",
        "37. Profitable Schemes.py",
        "38. Minimum Cost to Cut a Stick.py",
        "39. Painting the Walls.py",
        "40. Number of Ways to Stay in the Same Place After Some Steps.py",
        "41. String Compression II.py",
        "42. Minimum Difficulty of a Job Schedule.py",
        "43. Arithmetic Slices II.py",
        "44. K Inverse Pairs Array.py",
        "45. Cherry Pickup II.py",
        "46. Minimum Falling Path Sum II.py",
        "47. Freedom Trail.py"
    ],
    "15. Greedy": [
        "1. Buy Two Chocolates.py",
        "2. Lemonade Change.py",
        "3. Minimum Number of Moves to Seat Everyone.py",
        "4. Maximum Odd Binary Number.py",
        "5. Maximum Nesting Depth of the Parentheses.py",
        "6. Check if One String Swap Can Make Strings Equal.py",
        "7. Minimum Operations to Make Binary Array Elements Equal to One I.py",
        "8. Buildings With an Ocean View.py",
        "9. Minimum Length of String After Operations.py",
        "10. Construct K Palindrome Strings.py",
        "11. Separate Black and White Balls.py",
        "12. Minimum Increment to Make Array Unique.py",
        "13. Maximum Subarray.py",
        "14. Maximum Absolute Sum of Any Subarray.py",
        "15. Maximum Sum Circular Subarray.py",
        "16. Minimum Swaps to Group All 1's Together II.py",
        "17. Longest Turbulent Array.py",
        "18. Jump Game.py",
        "19. Jump Game II.py",
        "20. Jump Game VII.py",
        "21. Gas Station.py",
        "22. Hand of Straights.py",
        "23. Minimum Number of Changes to Make Binary String Beautiful.py",
        "24. Minimize Maximum of Array.py",
        "25. Minimum Difference Between Largest and Smallest Value in Three Moves.py",
        "26. Maximum Total Importance of Roads.py",
        "27. Minimum Number of Pushes to Type Word II.py",
        "28. Dota2 Senate.py",
        "29. Maximum Points You Can Obtain From Cards.py",
        "30. Merge Triplets to Form Target Triplet.py",
        "31. Partition Labels.py",
        "32. Valid Parenthesis String.py",
        "33. Check if a Parentheses String Can Be Valid.py",
        "34. Eliminate Maximum Number of Monsters.py",
        "35. Two City Scheduling.py",
        "36. Maximum Length of Pair Chain.py",
        "37. Best Sightseeing Pair.py",
        "38. Make Lexicographically Smallest Array by Swapping Elements.py",
        "39. Minimum Deletions to Make Character Frequencies Unique.py",
        "40. Minimum Deletions to Make String Balanced.py",
        "41. Candy.py",
        "42. Remove Colored Pieces if Both Neighbors are the Same Color.py",
        "43. Maximum Score From Removing Substrings.py",
        "44. Maximum Element After Decreasing and Rearranging.py",
        "45. Number of Laser Beams in a Bank.py",
        "46. Maximum Distance in Arrays.py",
        "47. Reveal Cards In Increasing Order.py",
        "48. Construct String With Repeat Limit.py",
        "49. Find Valid Matrix Given Row and Column Sums.py",
        "50. Score After Flipping Matrix.py",
        "51. Flip Columns For Maximum Number of Equal Rows.py",
        "52. Maximum Matrix Sum.py",
        "53. Make Two Arrays Equal by Reversing Subarrays.py",
        "54. Shortest Subarray to be Removed to Make Array Sorted.py",
        "55. Max Chunks To Make Sorted.py",
        "56. Maximum Swap.py",
        "57. Maximal Score After Applying K Operations.py",
        "58. Put Marbles in Bags.py",
        "59. Minimum Number of K Consecutive Bit Flips.py",
        "60. Maximum Score of a Good Subarray.py",
        "61. Find the Maximum Sum of Node Values.py",
        "62. Apply Operations to Maximize Score.py"
    ],
    "16. Intervals": [
        "1. Insert Interval.py",
        "2. Merge Intervals.py",
        "3. Non Overlapping Intervals.py",
        "4. Meeting Rooms.py",
        "5. Meeting Rooms II.py",
        "6. Meeting Rooms III.py",
        "7. Divide Intervals Into Minimum Number of Groups.py",
        "8. Remove Covered Intervals.py",
        "9. Minimum Number of Arrows to Burst Balloons.py",
        "10. The Number of the Smallest Unoccupied Chair.py",
        "11. Check if Grid can be Cut into Sections.py",
        "12. My Calendar I.py",
        "13. My Calendar II.py",
        "14. Count Days Without Meetings.py",
        "15. Minimum Interval to Include Each Query.py",
        "16. Data Stream as Disjoint Intervals.py"
    ],
    "17. Math & Geometry": [
        "1. Excel Sheet Column Title.py",
        "2. Greatest Common Divisor of Strings.py",
        "3. Insert Greatest Common Divisors in Linked List.py",
        "4. Count Odd Numbers in an Interval Range.py",
        "5. Matrix Diagonal Sum.py",
        "6. Calculate Money in Leetcode Bank.py",
        "7. Largest Odd Number in String.py",
        "8. Transpose Matrix.py",
        "9. Image Smoother.py",
        "10. Count of Matches in Tournament.py",
        "11. Water Bottles.py",
        "12. Largest Local Values in a Matrix.py",
        "13. Power of Four.py",
        "14. Lucky Numbers in a Matrix.py",
        "15. Maximum Points on a Line.py",
        "16. Magic Squares In Grid.py",
        "17. Rotate Image.py",
        "18. Spiral Matrix.py",
        "19. Spiral Matrix II.py",
        "20. Spiral Matrix III.py",
        "21. Spiral Matrix IV.py",
        "22. Set Matrix Zeroes.py",
        "23. Happy Number.py",
        "24. Plus One.py",
        "25. Palindrome Number.py",
        "26. Ugly Number.py",
        "27. Convert 1D Array Into 2D Array.py",
        "28. Shift 2D Grid.py",
        "29. Roman to Integer.py",
        "30. Integer to Roman.py",
        "31. Pow(x, n).py",
        "32. Find the Punishment Number of an Integer.py",
        "33. Check if Number is a Sum of Powers of Three.py",
        "34. Multiply Strings.py",
        "35. Detect Squares.py",
        "36. Robot Bounded In Circle.py",
        "37. Walking Robot Simulation.py",
        "38. Zigzag Conversion.py",
        "39. Rotating the Box.py",
        "40. Sum of Square Numbers.py",
        "41. Find Missing Observations.py",
        "42. Minimum Time Difference.py",
        "43. Minimum Operations to Make a Uni-Value Grid.py",
        "44. Largest Submatrix With Rearrangements.py",
        "45. Wildest Vertical Area Between Two Points Containing No Points.py",
        "46. Tuple with Same Product.py",
        "47. Lexicographical Numbers.py",
        "48. Find the Winner of the Circular Game.py",
        "49. Count Total Number of Colored Cells.py",
        "50. Prime Subtraction Operation.py",
        "51. Closest Prime Numbers in Range.py",
        "52. Minimum Number of One Bit Operations to Make Integers Zero.py",
        "53. K-th Smallest in Lexicographical Order.py",
        "54. Integer to English Words.py"
    ],
    "18. Bit Manipulation": [
        "1. Single Number.py",
        "2. Single Number III.py",
        "3. Number of 1 Bits.py",
        "4. Counting Bits.py",
        "5. Add Binary.py",
        "6. Minimum Bit Flips to Convert Number.py",
        "7. Reverse Bits.py",
        "8. Missing Number.py",
        "9. Shuffle the Array.py",
        "10. Add to Array-Form of Integer.py",
        "11. Find the Difference.py",
        "12. Power of Two.py",
        "13. Sum of Two Integers.py",
        "14. Reverse Integer.py",
        "15. Bitwise XOR of All Pairings.py",
        "16. Largest Combination With Bitwise AND Greater Than Zero.py",
        "17. XOR Queries of a Subarray.py",
        "18. Maximum XOR for Each Query.py",
        "19. Neighboring Bitwise XOR.py",
        "20. Shortest Subarray With OR at Least K II.py",
        "21. Bitwise AND of Numbers Range.py",
        "22. Find Kth Bit in Nth Binary String.py",
        "23. Count Triplets That Can Form Two Arrays of Equal XOR.py",
        "24. Minimum Array End.py",
        "25. Find if Array Can Be Sorted.py",
        "26. Longest Subarray With Maximum Bitwise AND.py",
        "27. Longest Nice Subarray.py",
        "28. Find the Longest Substring Containing Vowels in Even Counts.py",
        "29. Minimize XOR.py"
    ],
    "19. JavaScript": [
        "1. Create Hello World Function.js",
        "2. Counter.js",
        "3. Counter II.js",
        "4. Apply Transform over each Element in Array.js",
        "5. Filter Elements from Array.js",
        "6. Array Reduce Transformation.js",
        "7. Function Composition.js",
        "8. Allow One Function Call.js",
        "9. Memoize.js",
        "10. Curry.js",
        "11. Sleep.js",
        "12. Promise Time Limit.js",
        "13. Promise Pool.js",
        "14. Cache With Time Limit.js",
        "15. Debounce.js",
        "16. Throttle.js",
        "17. JSON Deep Equal.js",
        "18. Convert Object to JSON String.js",
        "19. Array of Objects to Matrix.js",
        "20. Difference Between Two Objects.js",
        "21. Chunk Array.js",
        "22. Flatten Deeply Nested Array.js",
        "23. Array Prototype Last.js",
        "24. Group By.js",
        "25. Check if Object Instance of Class.js",
        "26. Call Function with Custom Context.js",
        "27. Event Emitter.js",
        "28. Array Wrapper.js",
        "29. Generate Fibonacci Sequence.js",
        "30. Nested Array Generator.js"
    ]


}

base_dir = "NeetCode Practice"


if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for category, problems in categories.items():
    category_dir = os.path.join(base_dir, category)

    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
    

    for problem in problems:
        file_path = os.path.join(category_dir, problem)
        with open(file_path, "w") as file:
            problem_name = problem.split('. ', 1)[1].replace('.py', '')
            file.write(f"# {problem_name}\n")

print(f"Problem files have been organized in '{base_dir}' folder.")
