#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class User():
    def __init__(self, ttask):
        self.ttask = ttask
    
    def clock(self):
        if self.ttask > 0:
            self.ttask -= 1

class Server():
    def __init__(self, umax):
        self.users = []
        self.umax = umax

    def add_user(self, new_user=User):
        if len(self.users) >= self.umax:
            return False
        else:
            self.users.append(new_user)
            return True

    def clock(self):
        for u in self.users:
            u.clock()

        new_arr = []
        for user in self.users:
            if user.ttask != 0:
                new_arr.append(user)
        self.users = new_arr

class Balancer():
    def __init__(self, arr):
        self.ttask = arr[0]
        self.umax = arr[1]
        self.new_users = arr[2:]

        self.ticks = self.ttask + len(self.new_users)
        self.servers = []
        self.response = []

        self.run()

        self.output = self.output_()

    def get_servers_ttasks(self):
        servers = []
        for s in self.servers:
            server = []
            for u in s.users:
                server.append(u.ttask)
            servers.append(server)
        return servers

    def distribute_users(self, new_users):
        n = new_users

        while n > 0:
            if self.servers == []:
                s = Server(self.umax)
                s.add_user(User(self.ttask))
                self.servers.append(s)

                n -= 1
            else:
                flag = False

                for s in self.servers:
                    while len(s.users) < s.umax and n > 0:
                        s.add_user(User(self.ttask))

                        n -= 1
                        flag = True

                if flag == False:
                    s = Server(self.umax)
                    s.add_user(User(self.ttask))
                    self.servers.append(s)

                    n -= 1
                    
    def clock(self):
        for s in self.servers:
            s.clock()
        
        new_servers = []
        for s in self.servers:
            if s.users != []:
                new_servers.append(s)
        self.servers = new_servers

    def run(self):
        n = self.ticks

        for tick in range(1, n+1):
            self.clock()

            if tick <= len(self.new_users):
                new_users = self.new_users[tick-1]

                self.distribute_users(new_users)
                
                print({
                    'Tick': tick, 
                    'Input': self.new_users[tick-1], 
                    'Ttasks': self.get_servers_ttasks()
                    })
            else:
                print({
                    'Tick': tick, 
                    'Input': '-', 
                    'Ttasks': self.get_servers_ttasks()
                    })

            self.response.append([len(x) for x in self.get_servers_ttasks()])
            
    def output_(self):
        cost = 0
        res = []
        for r in self.response:
            if r == []:
                res.append([str(0)])
            else:
                res.append([','.join([str(x) for x in r])])
                cost += len(r)
        res.append([str(cost)])

        return '\n'.join([str(x[0]) for x in res])

if __name__ == '__main__':
    filename = sys.argv[1] # nome no arquivo passado como argumento pela linha de comando -> python main.py input.txt
    input_ = open(filename,'rt')

    vals = list(filter(lambda x: x != '\n', list(input_.read())))
    vals = [int(x) for x in vals]
            
    b = Balancer(vals)

    output_filename = 'output.txt'
    output_ = open(output_filename,'w')
    output_.write(b.output)
    output_.close()
