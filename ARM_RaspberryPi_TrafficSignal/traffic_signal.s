// assemble/compile: g++ traffic_signal.s -lwiringPi -g -o traffic_signal
.equ INPUT, 0
.equ OUTPUT, 1
.equ LOW, 0
.equ HIGH, 1

.equ TRAFFIC_GO_OUTPUT, 4
.equ TRAFFIC_SLOW_OUTPUT, 5
.equ TRAFFIC_STOP_OUTPUT, 27
.equ WALK_GO_OUTPUT, 0
.equ WALK_STOP_OUTPUT, 2
.equ COLLISION_OUTPUT, 25
.equ WALKING, 3

.equ BUTTON_INPUT, 6

.global main

.align 4
.section .rodata
message: .asciz "Button not pressed\n"
check_time: .word 150000

.align 4
.text
main:
	PUSH {LR}
	BL wiringPiSetup
	MOV R0, #BUTTON_INPUT
	MOV R1, #INPUT
	BL pinMode
	
	MOV R0, #TRAFFIC_GO_OUTPUT
	MOV R1, #OUTPUT
	BL pinMode
	MOV R0, #TRAFFIC_SLOW_OUTPUT
	MOV R1, #OUTPUT
	BL pinMode
	MOV R0, #TRAFFIC_STOP_OUTPUT
	MOV R1, #OUTPUT
	BL pinMode
	
	MOV R0, #WALK_GO_OUTPUT
	MOV R1, #OUTPUT
	BL pinMode
	MOV R0, #WALK_STOP_OUTPUT
	MOV R1, #OUTPUT
	BL pinMode
	
	MOV R0, #WALKING
	MOV R1, #INPUT
	BL pinMode
	MOV R0, #COLLISION_OUTPUT
	MOV R1, #OUTPUT
	BL pinMode

do_while:
	MOV R0, #BUTTON_INPUT
	BL digitalRead
	CMP R0, #HIGH
	BNE do_while
traffic:
	// start with traffic go
	MOV R0, #TRAFFIC_GO_OUTPUT
	MOV R1, #HIGH
	BL digitalWrite
	MOV R0, #WALK_STOP_OUTPUT
	MOV R1, #HIGH
	BL digitalWrite
	
	LDR R0, =#2000
	BL delay
	
	// if you walk when it's not your turn you get run over
	MOV R2, #0
	LDR R3, =check_time
	LDR R3, [R3]
	walk_press_check:
		CMP R2, R3
		BGT end_walk_press_check
		
		MOV R0, #WALKING
		BL digitalRead
		CMP R0, #HIGH
		BNE walk_press_check
		
		MOV R0, #TRAFFIC_GO_OUTPUT
		MOV R1, #LOW
		BL digitalWrite
		
		MOV R0, #TRAFFIC_STOP_OUTPUT
		MOV R1, #HIGH
		BL digitalWrite
		MOV R0, #WALK_STOP_OUTPUT
		MOV R1, #HIGH
		BL digitalWrite
		MOV R0, #COLLISION_OUTPUT
		MOV R1, #HIGH
		BL digitalWrite
	
		LDR R0, =#5000
		BL delay
	
		MOV R0, #TRAFFIC_STOP_OUTPUT
		MOV R1, #LOW
		BL digitalWrite
		MOV R0, #WALK_STOP_OUTPUT
		MOV R1, #LOW
		BL digitalWrite
		MOV R0, #COLLISION_OUTPUT
		MOV R1, #LOW
		BL digitalWrite
	
		B traffic
	end_walk_press_check:
	
	// traffic slow, walk go blink
	MOV R0, #TRAFFIC_GO_OUTPUT
	MOV R1, #LOW
	BL digitalWrite
	MOV R0, #WALK_STOP_OUTPUT
	MOV R1, #LOW
	BL digitalWrite
	
	MOV R0, #TRAFFIC_SLOW_OUTPUT
	MOV R1, #HIGH
	BL digitalWrite
	
	////for loop
	MOV R2, #0
	
	for_blink_walk_go:
	// if #108 or lower, doesn't loop. if #109 or higher, infinitely loops
		CMP R2, #108
		BGT end_for_blink_walk_go
		
		MOV R0, #WALK_GO_OUTPUT
		MOV R1, #HIGH
		BL digitalWrite
		LDR R0, =#750
		BL delay
		MOV R0, #WALK_GO_OUTPUT
		MOV R1, #LOW
		BL digitalWrite
		LDR R0, =#750
		BL delay
		
		ADD R2, #1
		B for_blink_walk_go
	end_for_blink_walk_go:
	/////
	// I wanted to loop through the blinking, but the branching is being
	// weird. I think it might have to do with how delay uses the
	// registers loaded? Or maybe exactly how CMP works. I don't know.
	MOV R0, #WALK_GO_OUTPUT
	MOV R1, #HIGH
	BL digitalWrite
	LDR R0, =#750
	BL delay
	MOV R0, #WALK_GO_OUTPUT
	MOV R1, #LOW
	BL digitalWrite
	LDR R0, =#750
	BL delay
	MOV R0, #WALK_GO_OUTPUT
	MOV R1, #HIGH
	BL digitalWrite
	LDR R0, =#750
	BL delay
	MOV R0, #WALK_GO_OUTPUT
	MOV R1, #LOW
	BL digitalWrite
	LDR R0, =#750
	BL delay
	
	LDR R0, =#250
	BL delay
	
	// traffic stop, walk go
	MOV R0, #TRAFFIC_SLOW_OUTPUT
	MOV R1, #LOW
	BL digitalWrite
	
	MOV R0, #TRAFFIC_STOP_OUTPUT
	MOV R1, #HIGH
	BL digitalWrite
	MOV R0, #WALK_GO_OUTPUT
	MOV R1, #HIGH
	BL digitalWrite
	
	LDR R0, =#3000
	BL delay
	
	MOV R0, #TRAFFIC_STOP_OUTPUT
	MOV R1, #LOW
	BL digitalWrite
	MOV R0, #WALK_GO_OUTPUT
	MOV R1, #LOW
	BL digitalWrite
	B do_while

end_do_while:
	MOV R0, #0
	POP {PC}
