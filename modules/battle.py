"""
Module containing the RPG battle system.
"""
from modules.utils import get_continue_input

class BattleSystem:
    def __init__(self):
        # Player stats
        self.hp = 100
        self.atk = 10
        self.mana = 100
        self.speed = 50
        self.skill1damage = 20
        self.skill2damage = 0  # This is a stun
        self.ultdamage = 50

        # Enemy stats
        self.enemy_hp = 100
        self.enemy_atk = 10
        self.enemy_mana = 100
        self.enemy_speed = 55
        self.enemy_skill = 20
        self.enemy_ultdamage = 40

        # Game state variables
        self.player_stunned = False
        self.enemy_stunned = False
        self.turn = 1
        
    def display_battle_start(self):
        print("=" * 50)
        print("          TURN-BASED RPG BATTLE")
        print("=" * 50)
        print(f"Player: HP={self.hp}, ATK={self.atk}, MANA={self.mana}, SPEED={self.speed}")
        print(f"Enemy:  HP={self.enemy_hp}, ATK={self.enemy_atk}, MANA={self.enemy_mana}, SPEED={self.enemy_speed}")
        print("=" * 50)

    def player_turn(self):
        """Handle player's turn"""
        if not self.player_stunned:
            print(f"\nPlayer's turn!")
            print(f"Player: HP={self.hp}, MANA={self.mana}")
            print(f"Enemy:  HP={self.enemy_hp}, MANA={self.enemy_mana}")
            
            print("\nChoose your action:")
            print("1. Normal Attack (ATK damage)")
            print("2. Skill 1 (20 damage, -20 mana)")
            print("3. Skill 2 (Stun enemy, -30 mana)")
            print("4. Ultimate (50 damage, -50 mana)")
            
            # Player input
            while True:
                try:
                    action = int(input("Enter your choice (1-4): "))
                    if action >= 1 and action <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Execute player action
            if action == 1:
                print(f"Player attacks for {self.atk} damage!")
                self.enemy_hp = self.enemy_hp - self.atk
            elif action == 2:
                if self.mana >= 20:
                    print(f"Player uses Skill 1 for {self.skill1damage} damage!")
                    self.enemy_hp = self.enemy_hp - self.skill1damage
                    self.mana = self.mana - 20
                else:
                    print("Not enough mana! Normal attack instead.")
                    self.enemy_hp = self.enemy_hp - self.atk
            elif action == 3:
                if self.mana >= 30:
                    print("Player uses Skill 2 - Enemy is stunned!")
                    self.enemy_stunned = True
                    self.mana = self.mana - 30
                else:
                    print("Not enough mana! Normal attack instead.")
                    self.enemy_hp = self.enemy_hp - self.atk
            elif action == 4:
                if self.mana >= 50:
                    print(f"Player uses Ultimate for {self.ultdamage} damage!")
                    self.enemy_hp = self.enemy_hp - self.ultdamage
                    self.mana = self.mana - 50
                else:
                    print("Not enough mana! Normal attack instead.")
                    self.enemy_hp = self.enemy_hp - self.atk
            
            get_continue_input()
            print()
        else:
            print("Player is stunned and cannot act!")
            self.player_stunned = False
            get_continue_input()
            print()

    def enemy_turn(self):
        """Handle enemy's turn"""
        if not self.enemy_stunned:
            print(f"\nEnemy's turn!")
            print(f"Player: HP={self.hp}, MANA={self.mana}")
            print(f"Enemy:  HP={self.enemy_hp}, MANA={self.enemy_mana}")
            
            # Enemy AI - simple pattern
            if self.turn % 3 == 1:
                # Normal attack
                print(f"Enemy attacks for {self.enemy_atk} damage!")
                self.hp = self.hp - self.enemy_atk
            elif self.turn % 3 == 2:
                # Skill attack
                if self.enemy_mana >= 25:
                    print(f"Enemy uses skill for {self.enemy_skill} damage!")
                    self.hp = self.hp - self.enemy_skill
                    self.enemy_mana = self.enemy_mana - 25
                else:
                    print("Enemy is low on mana! Normal attack instead.")
                    self.hp = self.hp - self.enemy_atk
            else:
                # Ultimate attack
                if self.enemy_mana >= 40:
                    print(f"Enemy uses ultimate for {self.enemy_ultdamage} damage!")
                    self.hp = self.hp - self.enemy_ultdamage
                    self.enemy_mana = self.enemy_mana - 40
                else:
                    print("Enemy is low on mana! Normal attack instead.")
                    self.hp = self.hp - self.enemy_atk
            
            get_continue_input()
            print()
        else:
            print("Enemy is stunned and cannot act!")
            self.enemy_stunned = False
            get_continue_input()
            print()

    def regenerate_mana(self):
        """Regenerate mana for both players"""
        if self.mana < 100:
            self.mana = min(100, self.mana + 10)
        if self.enemy_mana < 100:
            self.enemy_mana = min(100, self.enemy_mana + 10)

    def run_battle(self):
        """Run the main battle loop"""
        self.display_battle_start()
        
        while self.hp > 0 and self.enemy_hp > 0 and self.turn <= 20:
            print(f"\n--- TURN {self.turn} ---")
            
            # Determine who goes first based on speed
            player_first = self.speed >= self.enemy_speed
            
            # Execute turns
            if player_first:
                self.player_turn()
                if self.enemy_hp > 0:
                    self.enemy_turn()
            else:
                self.enemy_turn()
                if self.hp > 0:
                    self.player_turn()
            
            # Regenerate mana
            self.regenerate_mana()
            
            # End of turn status
            print(f"\nEnd of turn {self.turn}:")
            print(f"Player: HP={self.hp}, MANA={self.mana}")
            print(f"Enemy:  HP={self.enemy_hp}, MANA={self.enemy_mana}")
            print("-" * 30)
            
            get_continue_input()
            print()
            
            self.turn += 1
        
        return self.get_battle_result()
    
    def get_battle_result(self):
        """Return the battle result"""
        print("\n" + "=" * 50)
        if self.hp <= 0:
            print("          DEFEAT!")
            print("        Enemy wins!")
            print("        In the end, you slept very late and highly likely you'll wake up feeling uncomfortable and this start might lead to a chain of bad events..")
            return False
        elif self.enemy_hp <= 0:
            print("          VICTORY!")
            print("        Player wins!")
            print("        Completed a balanced and productive day! You sleep early and will wake up in a good mood.")
            return True
        else:
            print("          DRAW!")
            print("      Battle ended!")
            print("      You still slept late, but not late enough to ruin your day tomorrow, just not as refreshed.")
            return None
