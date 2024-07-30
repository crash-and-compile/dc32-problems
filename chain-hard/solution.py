#!/usr/bin/env python3
import sys

def build_graph(words):
    graph = {word: [] for word in words}
    for word in words:
        for potential_next in words:
            if word != potential_next and word[-1] == potential_next[0]:
                graph[word].append(potential_next)
    return graph

def dfs(graph, word, visited, current_chain):
    visited.add(word)
    current_chain.append(word)
    
    max_chain = current_chain[:]
    
    for neighbor in graph[word]:
        if neighbor not in visited:
            current_chain_result = dfs(graph, neighbor, visited, current_chain)
            if len("".join(current_chain_result)) > len("".join(max_chain)):
                max_chain = current_chain_result[:]
    
    visited.remove(word)
    current_chain.pop()
    
    return max_chain

def process_line(line):
    words = line.strip().split()
    if not words:
        return 0, []
    
    graph = build_graph(words)
    max_chain = []
    
    for word in words:
        visited = set()
        current_chain = []
        current_chain_result = dfs(graph, word, visited, current_chain)
        if len("".join(current_chain_result)) > len("".join(max_chain)):
            max_chain = current_chain_result
    
    max_chain_length = len("".join(max_chain))
    return max_chain_length, max_chain

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # Process non-empty lines
                    max_length, max_chain = process_line(line)
                    print(str(max_length))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py filename")
    else:
        main(sys.argv[1])

